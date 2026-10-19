// It Takes Two mod loader.
//
// Loaded by the game as version.dll.

#include <windows.h>

#include <algorithm>
#include <share.h>

#include <cstdio>
#include <map>
#include <mutex>
#include <set>
#include <string>
#include <vector>

#define FORWARD(name, ordinal) \
    __pragma(comment(linker, "/export:" #name "=\\\\.\\GLOBALROOT\\SystemRoot\\System32\\version.dll." #name ",@" #ordinal))
FORWARD(GetFileVersionInfoA, 1)
FORWARD(GetFileVersionInfoByHandle, 2)
FORWARD(GetFileVersionInfoExA, 3)
FORWARD(GetFileVersionInfoExW, 4)
FORWARD(GetFileVersionInfoSizeA, 5)
FORWARD(GetFileVersionInfoSizeExA, 6)
FORWARD(GetFileVersionInfoSizeExW, 7)
FORWARD(GetFileVersionInfoSizeW, 8)
FORWARD(GetFileVersionInfoW, 9)
FORWARD(VerFindFileA, 10)
FORWARD(VerFindFileW, 11)
FORWARD(VerInstallFileA, 12)
FORWARD(VerInstallFileW, 13)
FORWARD(VerLanguageNameA, 14)
FORWARD(VerLanguageNameW, 15)
FORWARD(VerQueryValueA, 16)
FORWARD(VerQueryValueW, 17)

namespace {

const wchar_t* const kAngelScriptDir = L"AngelScript";
const wchar_t* const kCompileFlag = L"-as-ignore-precompiled-data";

struct Entry {
    std::wstring Name;
    std::wstring Path;
    bool Directory;
};

std::wstring ScriptRoot;                                     // lowercase <game>\nuts\script
std::map<std::wstring, std::wstring> Files;                  // lowercase path relative to Nuts/Script -> mod file
std::map<std::wstring, std::wstring> Directories;            // same, for folders that mods contain
std::map<std::wstring, std::map<std::wstring, Entry>> Children;  // lowercase relative folder -> lowercase name -> entry

FILE* Log = nullptr;
std::mutex LogMutex;

decltype(&CreateFileW) RealCreateFileW;
decltype(&GetFileAttributesW) RealGetFileAttributesW;
decltype(&GetFileAttributesExW) RealGetFileAttributesExW;
decltype(&FindFirstFileW) RealFindFirstFileW;
decltype(&FindNextFileW) RealFindNextFileW;
decltype(&FindClose) RealFindClose;
decltype(&GetCommandLineW) RealGetCommandLineW;

void Logf(const wchar_t* format, ...) {
    if (!Log) return;
    std::lock_guard<std::mutex> lock(LogMutex);
    va_list args;
    va_start(args, format);
    vfwprintf(Log, format, args);
    va_end(args);
    fputwc(L'\n', Log);
    fflush(Log);
}

std::wstring Lower(std::wstring text) {
    if (!text.empty()) CharLowerBuffW(text.data(), static_cast<DWORD>(text.size()));
    return text;
}

std::wstring Parent(const std::wstring& path) {
    size_t slash = path.find_last_of(L'\\');
    return slash == std::wstring::npos ? L"" : path.substr(0, slash);
}

std::wstring Join(const std::wstring& folder, const std::wstring& name) {
    return folder.empty() ? name : folder + L"\\" + name;
}

// Lowercase path relative to Nuts/Script, or false if the path isn't under it.
bool ToScriptRelative(LPCWSTR path, std::wstring& relative) {
    if (!path || ScriptRoot.empty()) return false;
    std::wstring text = path;
    if (text.rfind(L"\\\\?\\", 0) == 0 && text.rfind(L"\\\\?\\UNC\\", 0) != 0) text.erase(0, 4);
    std::replace(text.begin(), text.end(), L'/', L'\\');
    wchar_t full[2048];
    DWORD length = GetFullPathNameW(text.c_str(), ARRAYSIZE(full), full, nullptr);
    if (length == 0 || length >= ARRAYSIZE(full)) return false;
    std::wstring lowered = Lower(full);
    while (lowered.size() > 3 && lowered.back() == L'\\') lowered.pop_back();
    if (lowered == ScriptRoot) {
        relative.clear();
        return true;
    }
    if (lowered.size() > ScriptRoot.size() && lowered.compare(0, ScriptRoot.size(), ScriptRoot) == 0 &&
        lowered[ScriptRoot.size()] == L'\\') {
        relative = lowered.substr(ScriptRoot.size() + 1);
        return true;
    }
    return false;
}

// The mod's file or folder for this path, or null.
const std::wstring* ModPath(LPCWSTR path) {
    std::wstring relative;
    if (!ToScriptRelative(path, relative)) return nullptr;
    auto file = Files.find(relative);
    if (file != Files.end()) return &file->second;
    auto folder = Directories.find(relative);
    return folder != Directories.end() ? &folder->second : nullptr;
}

bool Matches(const wchar_t* spec, const wchar_t* name) {
    if (wcscmp(spec, L"*.*") == 0) return true;
    const wchar_t* star = nullptr;
    const wchar_t* resume = nullptr;
    while (*name) {
        if (*spec == L'*') {
            star = spec++;
            resume = name;
        } else if (*spec == L'?' || towlower(*spec) == towlower(*name)) {
            ++spec;
            ++name;
        } else if (star) {
            spec = star + 1;
            name = ++resume;
        } else {
            return false;
        }
    }
    while (*spec == L'*') ++spec;
    return *spec == 0;
}

void AddFile(const std::wstring& relative, const std::wstring& path, const std::wstring& mod) {
    std::wstring key = Lower(relative);
    auto existing = Files.find(key);
    if (existing != Files.end()) Logf(L"  %s overrides another mod's %s", mod.c_str(), relative.c_str());
    Files[key] = path;

    // Register the file and its parent folders for directory listings.
    std::wstring child = relative;
    std::wstring childPath = path;
    bool directory = false;
    while (!child.empty()) {
        std::wstring parent = Parent(child);
        std::wstring name = child.substr(parent.empty() ? 0 : parent.size() + 1);
        Children[Lower(parent)][Lower(name)] = Entry{name, childPath, directory};
        if (directory) Directories[Lower(child)] = childPath;
        child = parent;
        childPath = Parent(childPath);
        directory = true;
    }
}

void ScanFolder(const std::wstring& folder, const std::wstring& relative, const std::wstring& mod, int& count) {
    WIN32_FIND_DATAW data;
    HANDLE find = FindFirstFileW((folder + L"\\*").c_str(), &data);
    if (find == INVALID_HANDLE_VALUE) return;
    do {
        std::wstring name = data.cFileName;
        if (name == L"." || name == L"..") continue;
        std::wstring path = folder + L"\\" + name;
        if (data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            ScanFolder(path, Join(relative, name), mod, count);
        } else {
            AddFile(Join(relative, name), path, mod);
            ++count;
        }
    } while (FindNextFileW(find, &data));
    FindClose(find);
}

void LoadMods(const std::wstring& modsRoot) {
    std::vector<std::wstring> mods;
    WIN32_FIND_DATAW data;
    HANDLE find = FindFirstFileW((modsRoot + L"\\*").c_str(), &data);
    if (find != INVALID_HANDLE_VALUE) {
        do {
            std::wstring name = data.cFileName;
            if ((data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) && name != L"." && name != L"..") mods.push_back(name);
        } while (FindNextFileW(find, &data));
        FindClose(find);
    }
    std::sort(mods.begin(), mods.end(), [](const std::wstring& a, const std::wstring& b) { return Lower(a) < Lower(b); });
    for (const std::wstring& mod : mods) {
        std::wstring scripts = modsRoot + L"\\" + mod + L"\\" + kAngelScriptDir;
        DWORD attributes = GetFileAttributesW(scripts.c_str());
        if (attributes == INVALID_FILE_ATTRIBUTES || !(attributes & FILE_ATTRIBUTE_DIRECTORY)) {
            Logf(L"%s: no %s folder, nothing to load", mod.c_str(), kAngelScriptDir);
            continue;
        }
        int count = 0;
        ScanFolder(scripts, L"", mod, count);
        Logf(L"%s: %d script file(s)", mod.c_str(), count);
    }
}

// A directory listing: the real entries first, then any extra files the mods add.
struct Listing {
    HANDLE Real;
    bool HavePending;
    WIN32_FIND_DATAW Pending;
    std::wstring Folder;
    std::wstring Spec;
    std::set<std::wstring> Seen;
    std::vector<const Entry*> Extra;
    size_t NextExtra;
    bool ExtraBuilt;
};

std::set<Listing*> Listings;
std::mutex ListingsMutex;

bool IsListing(HANDLE handle, Listing*& listing) {
    std::lock_guard<std::mutex> lock(ListingsMutex);
    listing = static_cast<Listing*>(handle);
    return Listings.count(listing) != 0;
}

void FillFromPath(const std::wstring& path, const std::wstring& name, WIN32_FIND_DATAW* data) {
    WIN32_FILE_ATTRIBUTE_DATA attributes{};
    RealGetFileAttributesExW(path.c_str(), GetFileExInfoStandard, &attributes);
    ZeroMemory(data, sizeof(*data));
    data->dwFileAttributes = attributes.dwFileAttributes;
    data->ftCreationTime = attributes.ftCreationTime;
    data->ftLastAccessTime = attributes.ftLastAccessTime;
    data->ftLastWriteTime = attributes.ftLastWriteTime;
    data->nFileSizeHigh = attributes.nFileSizeHigh;
    data->nFileSizeLow = attributes.nFileSizeLow;
    wcsncpy_s(data->cFileName, name.c_str(), _TRUNCATE);
}

bool NextEntry(Listing* listing, WIN32_FIND_DATAW* data) {
    while (listing->Real != INVALID_HANDLE_VALUE) {
        if (listing->HavePending) {
            *data = listing->Pending;
            listing->HavePending = false;
        } else if (!RealFindNextFileW(listing->Real, data)) {
            RealFindClose(listing->Real);
            listing->Real = INVALID_HANDLE_VALUE;
            break;
        }
        std::wstring name = Lower(data->cFileName);
        listing->Seen.insert(name);
        auto file = Files.find(Join(listing->Folder, name));
        if (file != Files.end()) FillFromPath(file->second, data->cFileName, data);
        return true;
    }
    if (!listing->ExtraBuilt) {
        listing->ExtraBuilt = true;
        auto children = Children.find(listing->Folder);
        if (children != Children.end()) {
            for (const auto& [name, entry] : children->second) {
                if (!listing->Seen.count(name) && Matches(listing->Spec.c_str(), entry.Name.c_str())) {
                    listing->Extra.push_back(&entry);
                }
            }
        }
    }
    if (listing->NextExtra >= listing->Extra.size()) return false;
    const Entry* entry = listing->Extra[listing->NextExtra++];
    FillFromPath(entry->Path, entry->Name, data);
    return true;
}

HANDLE WINAPI HookFindFirstFileW(LPCWSTR pattern, LPWIN32_FIND_DATAW data) {
    std::wstring relative;
    if (!pattern || !ToScriptRelative(pattern, relative) || relative.empty()) return RealFindFirstFileW(pattern, data);
    std::wstring folder = Parent(relative);
    if (!Children.count(folder)) return RealFindFirstFileW(pattern, data);

    std::wstring patternText = pattern;
    size_t slash = patternText.find_last_of(L"\\/");
    auto* listing = new Listing{};
    listing->Folder = folder;
    listing->Spec = slash == std::wstring::npos ? patternText : patternText.substr(slash + 1);
    listing->Real = RealFindFirstFileW(pattern, &listing->Pending);
    listing->HavePending = listing->Real != INVALID_HANDLE_VALUE;
    if (!NextEntry(listing, data)) {
        if (listing->Real != INVALID_HANDLE_VALUE) RealFindClose(listing->Real);
        delete listing;
        SetLastError(ERROR_FILE_NOT_FOUND);
        return INVALID_HANDLE_VALUE;
    }
    std::lock_guard<std::mutex> lock(ListingsMutex);
    Listings.insert(listing);
    return listing;
}

BOOL WINAPI HookFindNextFileW(HANDLE handle, LPWIN32_FIND_DATAW data) {
    Listing* listing;
    if (!IsListing(handle, listing)) return RealFindNextFileW(handle, data);
    if (NextEntry(listing, data)) return TRUE;
    SetLastError(ERROR_NO_MORE_FILES);
    return FALSE;
}

BOOL WINAPI HookFindClose(HANDLE handle) {
    Listing* listing;
    if (!IsListing(handle, listing)) return RealFindClose(handle);
    {
        std::lock_guard<std::mutex> lock(ListingsMutex);
        Listings.erase(listing);
    }
    if (listing->Real != INVALID_HANDLE_VALUE) RealFindClose(listing->Real);
    delete listing;
    return TRUE;
}

HANDLE WINAPI HookCreateFileW(LPCWSTR name, DWORD access, DWORD share, LPSECURITY_ATTRIBUTES security,
                              DWORD disposition, DWORD flags, HANDLE templateFile) {
    const DWORD writeAccess = GENERIC_WRITE | GENERIC_ALL | FILE_WRITE_DATA | FILE_APPEND_DATA | DELETE;
    if (disposition == OPEN_EXISTING && !(access & writeAccess)) {
        std::wstring relative;
        if (ToScriptRelative(name, relative)) {
            auto file = Files.find(relative);
            if (file != Files.end()) {
                Logf(L"Opened %s -> %s", relative.c_str(), file->second.c_str());
                return RealCreateFileW(file->second.c_str(), access, share, security, disposition, flags, templateFile);
            }
        }
    }
    return RealCreateFileW(name, access, share, security, disposition, flags, templateFile);
}

DWORD WINAPI HookGetFileAttributesW(LPCWSTR name) {
    const std::wstring* path = ModPath(name);
    return RealGetFileAttributesW(path ? path->c_str() : name);
}

BOOL WINAPI HookGetFileAttributesExW(LPCWSTR name, GET_FILEEX_INFO_LEVELS level, LPVOID info) {
    const std::wstring* path = ModPath(name);
    return RealGetFileAttributesExW(path ? path->c_str() : name, level, info);
}

LPWSTR WINAPI HookGetCommandLineW() {
    static std::wstring commandLine;
    static std::once_flag once;
    std::call_once(once, [] {
        commandLine = RealGetCommandLineW();
        if (!Files.empty() && Lower(commandLine).find(kCompileFlag) == std::wstring::npos) {
            commandLine += L" ";
            commandLine += kCompileFlag;
            Logf(L"Added %s to the command line", kCompileFlag);
        }
    });
    return commandLine.data();
}

// Redirects the game's file functions to the hooks above.
void PatchImports() {
    struct Hook {
        const char* Name;
        void* Replacement;
        void** Original;
    };
    Hook hooks[] = {
        {"CreateFileW", reinterpret_cast<void*>(&HookCreateFileW), reinterpret_cast<void**>(&RealCreateFileW)},
        {"GetFileAttributesW", reinterpret_cast<void*>(&HookGetFileAttributesW), reinterpret_cast<void**>(&RealGetFileAttributesW)},
        {"GetFileAttributesExW", reinterpret_cast<void*>(&HookGetFileAttributesExW), reinterpret_cast<void**>(&RealGetFileAttributesExW)},
        {"FindFirstFileW", reinterpret_cast<void*>(&HookFindFirstFileW), reinterpret_cast<void**>(&RealFindFirstFileW)},
        {"FindNextFileW", reinterpret_cast<void*>(&HookFindNextFileW), reinterpret_cast<void**>(&RealFindNextFileW)},
        {"FindClose", reinterpret_cast<void*>(&HookFindClose), reinterpret_cast<void**>(&RealFindClose)},
        {"GetCommandLineW", reinterpret_cast<void*>(&HookGetCommandLineW), reinterpret_cast<void**>(&RealGetCommandLineW)},
    };

    auto* base = reinterpret_cast<BYTE*>(GetModuleHandleW(nullptr));
    auto* dos = reinterpret_cast<IMAGE_DOS_HEADER*>(base);
    auto* nt = reinterpret_cast<IMAGE_NT_HEADERS*>(base + dos->e_lfanew);
    const IMAGE_DATA_DIRECTORY& directory = nt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];
    auto* descriptor = reinterpret_cast<IMAGE_IMPORT_DESCRIPTOR*>(base + directory.VirtualAddress);
    int patched = 0;
    for (; descriptor->Name; ++descriptor) {
        if (_stricmp(reinterpret_cast<char*>(base + descriptor->Name), "KERNEL32.dll") != 0) continue;
        if (!descriptor->OriginalFirstThunk) continue;
        auto* names = reinterpret_cast<IMAGE_THUNK_DATA*>(base + descriptor->OriginalFirstThunk);
        auto* slots = reinterpret_cast<IMAGE_THUNK_DATA*>(base + descriptor->FirstThunk);
        for (; names->u1.AddressOfData; ++names, ++slots) {
            if (IMAGE_SNAP_BY_ORDINAL(names->u1.Ordinal)) continue;
            auto* import = reinterpret_cast<IMAGE_IMPORT_BY_NAME*>(base + names->u1.AddressOfData);
            for (Hook& hook : hooks) {
                if (strcmp(import->Name, hook.Name) != 0) continue;
                *hook.Original = reinterpret_cast<void*>(slots->u1.Function);
                DWORD protection;
                VirtualProtect(&slots->u1.Function, sizeof(void*), PAGE_READWRITE, &protection);
                slots->u1.Function = reinterpret_cast<ULONG_PTR>(hook.Replacement);
                VirtualProtect(&slots->u1.Function, sizeof(void*), protection, &protection);
                ++patched;
            }
        }
    }
    Logf(L"Hooked %d of %d file functions", patched, static_cast<int>(ARRAYSIZE(hooks)));
}

void Start() {
    // <game>\Nuts\Binaries\Win64\ItTakesTwo.exe -> <game>
    wchar_t exe[MAX_PATH];
    GetModuleFileNameW(nullptr, exe, MAX_PATH);
    std::wstring nuts = Parent(Parent(Parent(exe)));
    std::wstring game = Parent(nuts);
    std::wstring modsRoot = game + L"\\Mods";
    CreateDirectoryW(modsRoot.c_str(), nullptr);
    Log = _wfsopen((modsRoot + L"\\ModLoader.log").c_str(), L"w, ccs=UTF-8", _SH_DENYWR);
    Logf(L"It Takes Two mod loader. Mods folder: %s", modsRoot.c_str());

    ScriptRoot = Lower(nuts + L"\\Script");
    LoadMods(modsRoot);
    if (Files.empty()) {
        Logf(L"No mod scripts, game files are left alone");
        return;
    }
    PatchImports();
}

}  // namespace

BOOL WINAPI DllMain(HINSTANCE instance, DWORD reason, LPVOID) {
    if (reason == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(instance);
        Start();
    }
    return TRUE;
}
