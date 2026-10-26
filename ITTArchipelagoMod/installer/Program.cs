// Installs the It Takes Two Archipelago mod (mod loader, UE4SS and the Lua mod) from the embedded payload.zip.
// No game files are replaced.

using System.Diagnostics;
using System.IO.Compression;
using System.Reflection;
using Microsoft.Win32;

const string ModPrefix = "ArchipelagoITT";
const string ModName = ModPrefix + "v0.1.2";
const string BackupSuffix = ".ap-backup";  // left by older versions

Console.Title = "It Takes Two Archipelago mod installer";
Console.WriteLine("It Takes Two Archipelago mod installer");
Console.WriteLine();
try
{
    Run();
}
catch (Exception error)
{
    Console.WriteLine();
    Console.WriteLine($"Something went wrong: {error.Message}");
}
Console.WriteLine();
Console.Write("Press Enter to close.");
Console.ReadLine();

void Run()
{
    // A folder dropped onto the exe is used over Steam's.
    string? game = args.Length > 0 ? GameFolderFrom(args[0]) : FindGame();
    while (game == null)
    {
        Console.WriteLine("Couldn't find It Takes Two. In Steam, right-click It Takes Two > Manage > Browse local files,");
        Console.WriteLine("then drag that folder into this window (or paste its path) and press Enter.");
        Console.Write("> ");
        string? typed = Console.ReadLine()?.Trim().Trim('"');
        if (string.IsNullOrEmpty(typed)) return;
        game = GameFolderFrom(typed);
    }
    Console.WriteLine($"It Takes Two folder: {game}");
    Console.WriteLine();

    bool installed = ModFolders(game).Any(folder => File.Exists(Path.Combine(folder, "Scripts", "main.lua")));
    Console.WriteLine(installed ? "The mod is already installed." : "The mod is not installed yet.");
    Console.WriteLine(installed ? "  [Enter] Update / repair    [U] Uninstall    [Q] Quit" : "  [Enter] Install    [Q] Quit");
    Console.Write("> ");
    string choice = (Console.ReadLine() ?? "").Trim().ToUpperInvariant();
    if (choice == "Q") return;
    bool uninstall = installed && choice == "U";

    while (Process.GetProcessesByName("ItTakesTwo").Length > 0)
    {
        Console.Write("It Takes Two is running. Close it, then press Enter.");
        Console.ReadLine();
    }

    if (uninstall) Uninstall(game);
    else Install(game);
}

// The game folder from Steam.
string? FindGame()
{
    foreach (RegistryView view in new[] { RegistryView.Registry64, RegistryView.Registry32 })
    {
        using RegistryKey root = RegistryKey.OpenBaseKey(RegistryHive.LocalMachine, view);
        using RegistryKey? key = root.OpenSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 1426210");
        if (key?.GetValue("InstallLocation") is string location && GameFolderFrom(location) is string game) return game;
    }
    return GameFolderFrom(@"C:\Program Files (x86)\Steam\steamapps\common\ItTakesTwo");
}

// The game folder that contains this path.
string? GameFolderFrom(string path)
{
    try
    {
        for (DirectoryInfo? folder = new(Path.GetFullPath(path)); folder != null; folder = folder.Parent)
        {
            if (File.Exists(Path.Combine(folder.FullName, "Nuts", "Binaries", "Win64", "ItTakesTwo.exe"))) return folder.FullName;
        }
    }
    catch (Exception)
    {
        // Not a usable path.
    }
    return null;
}

void Install(string game)
{
    string win64 = Path.Combine(game, "Nuts", "Binaries", "Win64");
    DeleteModFolders(game);
    DeleteFolder(Path.Combine(win64, "ue4ss", "Mods", ModPrefix));
    RestoreBackups(game);

    using Stream payload = Assembly.GetExecutingAssembly().GetManifestResourceStream("payload.zip")
        ?? throw new InvalidOperationException("this installer is missing its files");
    using ZipArchive archive = new(payload);
    int count = 0;
    foreach (ZipArchiveEntry entry in archive.Entries)
    {
        if (entry.FullName.EndsWith('/')) continue;
        string destination = Path.GetFullPath(Path.Combine(game, entry.FullName));
        Directory.CreateDirectory(Path.GetDirectoryName(destination)!);
        entry.ExtractToFile(destination, overwrite: true);
        count++;
    }
    Console.WriteLine($"Installed {count} files.");
    Console.WriteLine();
    Console.WriteLine("Done. The mod does nothing until the Archipelago It Takes Two Client is connected.");
}

void Uninstall(string game)
{
    string win64 = Path.Combine(game, "Nuts", "Binaries", "Win64");
    DeleteFile(Path.Combine(win64, "version.dll"));
    DeleteFile(Path.Combine(win64, "dwmapi.dll"));
    DeleteFolder(Path.Combine(win64, "ue4ss"));
    DeleteModFolders(game);
    DeleteFile(Path.Combine(game, "Mods", "ModLoader.log"));
    RestoreBackups(game);
    Console.WriteLine("Uninstalled. The game is back to normal.");
}

// This mod's folders in <game>/Mods, from any version (ArchipelagoITT, ArchipelagoITTv0.1.2, ...).
IEnumerable<string> ModFolders(string game)
{
    string mods = Path.Combine(game, "Mods");
    return Directory.Exists(mods) ? Directory.GetDirectories(mods, ModPrefix + "*") : [];
}

// The loader loads every folder in Mods, so an older version's folder left behind would load twice.
void DeleteModFolders(string game)
{
    foreach (string folder in ModFolders(game)) DeleteFolder(folder);
}

// Restores game scripts replaced by older versions.
void RestoreBackups(string game)
{
    string scripts = Path.Combine(game, "Nuts", "Script");
    if (!Directory.Exists(scripts)) return;
    foreach (string backup in Directory.EnumerateFiles(scripts, "*" + BackupSuffix, SearchOption.AllDirectories))
    {
        File.Move(backup, backup[..^BackupSuffix.Length], overwrite: true);
        Console.WriteLine($"Restored original {Path.GetFileName(backup[..^BackupSuffix.Length])}");
    }
}

void DeleteFile(string path)
{
    if (File.Exists(path)) File.Delete(path);
}

void DeleteFolder(string path)
{
    if (Directory.Exists(path)) Directory.Delete(path, recursive: true);
}
