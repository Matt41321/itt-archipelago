-- Talks to the client through files in %LOCALAPPDATA%\ItTakesTwoArchipelago:
--   ap_state.txt   unlocked items, written by the client
--   checks.txt     checks sent, one per line, read by the client
--   heartbeat.txt  updated by the client while connected
-- If the client isn't connected, the mod does nothing.

local Chapters = require("chapters")
local Checkpoints = require("checkpoints")

local BridgeDir = (os.getenv("LOCALAPPDATA") or ".") .. "\\ItTakesTwoArchipelago\\"
local StateFile = BridgeDir .. "ap_state.txt"
local ChecksFile = BridgeDir .. "checks.txt"
local LastChapterFile = BridgeDir .. "last_chapter.txt"
local HeartbeatFile = BridgeDir .. "heartbeat.txt"

local PollMs = 500
local MenuPollMs = 100
local KickCooldownSeconds = 10
local HeartbeatTimeoutSeconds = 5

-- Must match MOVEMENT_ITEMS in items.py.
local MovementTags = { "AirJump", "Dash", "GroundPound", "WallSlide", "Swinging", "Grinding",
                       "SprintActivation", "SlopeSlide", "LedgeGrab" }

-- Extra tags blocked for a movement item. Dash also covers the slide dash, long jump and grinding dash.
local MovementBlocks = {
    Dash = { "Dash", "DashAction", "LongJump", "GrindingDash" },
}

-- Blocked with an exclusion so the patched air jump reset keeps running.
local BlockExclusions = {
    AirJump = "ArchipelagoKeep",
}

local function MovementBlockTags(Tag)
    return MovementBlocks[Tag] or { Tag }
end

-- Ability item -> capability tags. Owner limits the block to one character. Must match ABILITIES in items.py.
local Abilities = {
    ["Shed May Ability"] = { Tags = { "HammerWeapon", "HammerSmash", "WeaponHammer" } },
    ["Shed Cody Ability"] = { Tags = { "NailWeapon" } },
    ["Tree May Ability"] = { Tags = { "MatchWeapon" } },
    ["Tree Cody Ability"] = { Tags = { "SapWeapon" } },
    ["Rose's Room May Ability"] = { Tags = { "Gravity" }, Owner = "May" },
    ["Rose's Room Cody Ability"] = { Tags = { "ChangeSize", "MutuallyExclusiveSize" } },
    ["Cuckoo Clock May Ability"] = { Tags = { "TimeSequenceCapability", "Sequence" } },
    ["Cuckoo Clock Cody Ability"] = { Tags = { "TimeControlCapability", "TimeControlling" } },
    ["Snow Globe Ability"] = { Tags = { "MagneticCapability", "MagnetCapability", "MagneticPlayerAttraction", "PlayerMagnetLaunch" } },
    ["Garden May Ability"] = { Tags = { "WaterHose", "SickleName", "SickleAttackName" } },
    ["Garden Cody Ability"] = { Tags = { "Vine" } },
    ["Attic May Ability"] = { Tags = { "PowerfulSong", "SongOfLife" } },
    ["Attic Cody Ability"] = { Tags = { "Cymbal", "CymbalShield" } },
}

local FinalChapter = "A Grand Finale"
local GoalLine = "!goal" -- must match GOAL_LINE in client.py

local function Log(Msg)
    print("[Archipelago] " .. Msg .. "\n")
end

------------------------------------------------------------------------------------------------------------------------
-- Chapter lookups

-- "VacuumIntro (Shed/Vacuum)" -> "Shed"
local function MapRoot(Key)
    return Key:match("%(([^/%)]+)")
end

local ChapterByKey = {}
local ChapterByName = {}
local ChapterByMinigameId = {}
local NextStoryChapter = {}
local GroupByMapRoot = {}
local MinigameOrder = {}
do
    local Previous = nil
    for _, Chapter in ipairs(Chapters) do
        ChapterByKey[Chapter.key] = Chapter
        ChapterByName[Chapter.name] = Chapter
        if not Chapter.is_minigame then
            GroupByMapRoot[MapRoot(Chapter.key)] = Chapter.group
        end
        if Chapter.is_minigame then
            ChapterByMinigameId[Chapter.minigame_id] = Chapter
            table.insert(MinigameOrder, Chapter)
        else
            if Previous then
                NextStoryChapter[Previous.name] = Chapter.name
            end
            Previous = Chapter
        end
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Bridge files

local function ReadLines(Path)
    local File = io.open(Path, "r")
    if not File then return nil end
    local Lines = {}
    for Line in File:lines() do
        table.insert(Lines, (Line:gsub("\r$", "")))
    end
    File:close()
    return Lines
end

local function WriteFile(Path, Text)
    local File = io.open(Path, "w")
    if not File then return end
    File:write(Text)
    File:close()
end

local LastHeartbeat = nil
local LastStateLines = nil

-- Returns nil when the client isn't connected.
local function ReadState()
    local Heartbeat = tonumber((ReadLines(HeartbeatFile) or {})[1]) or LastHeartbeat
    LastHeartbeat = Heartbeat
    if not Heartbeat or math.abs(os.time() - Heartbeat) > HeartbeatTimeoutSeconds then return nil end
    local Lines = ReadLines(StateFile)
    if Lines and Lines[1] == "connected" then
        LastStateLines = Lines
    else
        Lines = LastStateLines
    end
    if not Lines then return nil end
    local State = { Moves = {}, Abilities = {}, Chapters = {}, Groups = {}, Minigames = {} }
    for _, Line in ipairs(Lines) do
        local Kind, Value = Line:match("^(%a+):(.+)$")
        if Kind == "move" then
            State.Moves[Value] = true
        elseif Kind == "ability" then
            State.Abilities[Value] = true
        elseif Kind == "chapter" and ChapterByName[Value] then
            State.Chapters[Value] = true
            State.Groups[ChapterByName[Value].group] = true
        elseif Kind == "minigame" then
            State.Minigames[Value] = true
        end
    end
    return State
end

local function SendCheck(LocationName)
    for _, Line in ipairs(ReadLines(ChecksFile) or {}) do
        if Line == LocationName then return end
    end
    local File = io.open(ChecksFile, "a")
    if not File then
        Log("Could not write " .. ChecksFile)
        return
    end
    File:write(LocationName .. "\n")
    File:close()
    Log("Check: " .. LocationName)
end

------------------------------------------------------------------------------------------------------------------------
-- Game access

local CapabilityStatics = nil
local ProgressStatics = nil

local function Statics()
    if not CapabilityStatics or not CapabilityStatics:IsValid() then
        CapabilityStatics = StaticFindObject("/Script/Nuts.Default__HazeCapabilityStatics")
    end
    if not ProgressStatics or not ProgressStatics:IsValid() then
        ProgressStatics = StaticFindObject("/Script/Nuts.Default__HazeProgressStatics")
    end
    return CapabilityStatics, ProgressStatics
end

local function Players()
    local Result = {}
    for _, Player in ipairs(FindAllOf("HazePlayerCharacter") or {}) do
        if Player:IsValid() then
            table.insert(Result, Player)
        end
    end
    return Result
end

------------------------------------------------------------------------------------------------------------------------
-- Movement and ability locks.

local BlockedOn = {}

local function PlayerKey(Player)
    return string.format("%s@%x", Player:GetFName():ToString(), Player:GetAddress())
end

local function WantedBlocks(State, Player)
    local Want = {}
    if not State then return Want end
    for _, Tag in ipairs(MovementTags) do
        if not State.Moves[Tag] then
            for _, Blocked in ipairs(MovementBlockTags(Tag)) do Want[Blocked] = true end
        end
    end
    local Name = Player:GetFName():ToString()
    for Item, Ability in pairs(Abilities) do
        if not State.Abilities[Item] and (not Ability.Owner or Name:find("^" .. Ability.Owner)) then
            for _, Tag in ipairs(Ability.Tags) do Want[Tag] = true end
        end
    end
    return Want
end

local AllBlockableTags = {}
for _, Tag in ipairs(MovementTags) do
    for _, Blocked in ipairs(MovementBlockTags(Tag)) do table.insert(AllBlockableTags, Blocked) end
end
for _, Ability in pairs(Abilities) do
    for _, Tag in ipairs(Ability.Tags) do table.insert(AllBlockableTags, Tag) end
end

-- Blocks don't reach capabilities added later (level loads, restarts), so for a while after those
-- every block is reapplied repeatedly.
local SettleSeconds = 12
local SettleMs = 250
local SettleUntil = 0

local function StartSettle(Reason)
    if os.time() >= SettleUntil then Log("Settling locks: " .. Reason) end
    SettleUntil = os.time() + SettleSeconds
end

local function Settling()
    return os.time() < SettleUntil
end

local ExcludingWorks = true

local function Block(Capabilities, Player, Tag)
    local Exclusion = BlockExclusions[Tag]
    if Exclusion and ExcludingWorks then
        local Ok, Err = pcall(function()
            Capabilities:BlockCapabilitiesExcluding(Player, FName(Tag), FName(Exclusion), Player)
        end)
        if Ok then return end
        ExcludingWorks = false
        Log("BlockCapabilitiesExcluding failed (" .. tostring(Err) .. "); blocking without exclusions")
    end
    Capabilities:BlockCapabilities(Player, FName(Tag), Player)
end

local function ApplyBlocks(State, PlayerList, Capabilities, Reblock)
    local Seen = {}
    for _, Player in ipairs(PlayerList) do
        local Key = PlayerKey(Player)
        Seen[Key] = true
        if not BlockedOn[Key] then StartSettle("new player " .. Player:GetFName():ToString()) end
        local Blocked = BlockedOn[Key] or {}
        BlockedOn[Key] = Blocked
        if Reblock then
            for Tag in pairs(Blocked) do
                Capabilities:UnblockCapabilities(Player, FName(Tag), Player)
                Block(Capabilities, Player, Tag)
            end
        end
        local Wanted = WantedBlocks(State, Player)
        for _, Tag in ipairs(AllBlockableTags) do
            local Want = Wanted[Tag] == true
            if Want and not Blocked[Tag] then
                Block(Capabilities, Player, Tag)
                Blocked[Tag] = true
                Log("Blocked " .. Tag .. " on " .. Player:GetFName():ToString())
            elseif not Want and Blocked[Tag] then
                Capabilities:UnblockCapabilities(Player, FName(Tag), Player)
                Blocked[Tag] = nil
                Log("Unblocked " .. Tag .. " on " .. Player:GetFName():ToString())
            end
        end
    end
    for Key in pairs(BlockedOn) do
        if not Seen[Key] then BlockedOn[Key] = nil end
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Chapter progress: completion checks, and kicking players out of locked chapters.

local LastActivePoint = nil
local LastChapter = (ReadLines(LastChapterFile) or {})[1]
local CurrentChapter = nil
local LastKickTime = 0

local PickerChapter = nil
local PickerSeenTime = 0
local ChapterSelectWindowSeconds = 60

local function CameFromChapterSelect(Chapter)
    return PickerChapter == Chapter.name and os.time() - PickerSeenTime <= ChapterSelectWindowSeconds
end

local function OnEnterChapter(State, Chapter, Player, Progress)
    if CameFromChapterSelect(Chapter) then
        Log("Entered " .. Chapter.name .. " from chapter select; no completion check")
        if not State.Chapters[Chapter.name] and os.time() - LastKickTime > KickCooldownSeconds then
            LastKickTime = os.time()
            Log(Chapter.name .. " is locked and was picked in chapter select; returning to main menu")
            Progress:ReturnToMainMenu(Player, nil)
            return
        end
    elseif LastChapter and NextStoryChapter[LastChapter] == Chapter.name and LastChapter ~= FinalChapter then
        SendCheck(LastChapter .. " Complete")
    end
    PickerChapter = nil
    LastChapter = Chapter.name
    WriteFile(LastChapterFile, LastChapter .. "\n")
end

local function SendCheckpoint(State, Key)
    if State and Checkpoints[Key] and os.time() - LastKickTime > KickCooldownSeconds then
        SendCheck("cp:" .. Key)
    end
end

local function ApplyProgress(State, PlayerList, Progress)
    local Player = PlayerList[1]
    if not Player then return end

    local Active = Progress:DebugGetActiveProgressPoint(Player):ToString()
    if Active ~= LastActivePoint then
        LastActivePoint = Active
        Log("Progress point: " .. Active)
        StartSettle("progress point " .. Active)
        local Chapter = ChapterByKey[Active]
        if Chapter and not Chapter.is_minigame then
            Log("Entered chapter: " .. Chapter.name .. " (" .. Chapter.group .. ")")
            CurrentChapter = Chapter
            if State then OnEnterChapter(State, Chapter, Player, Progress) end
        end
        SendCheckpoint(State, Active)
    end

    local Group = GroupByMapRoot[MapRoot(Active) or ""]
    if CurrentChapter and Group ~= CurrentChapter.group then
        CurrentChapter = nil
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Patched scripts. Only touch their properties once the patch is confirmed loaded; a missing property crashes UE4SS.

local PatchedClass = {}
local WarnedUnpatched = false

local function PathOf(Object)
    return Object:GetFullName():match("^%S+%s+(.+)$")
end

-- Walks up the class chain, since widgets are Blueprint subclasses of the patched class.
local function ClassHasFunction(Class, FunctionName)
    for _ = 1, 8 do
        if not Class or not Class:IsValid() then return false end
        local Path = PathOf(Class)
        if Path then
            local Function = StaticFindObject(Path .. ":" .. FunctionName)
            if Function and Function:IsValid() then return true end
        end
        Class = Class:GetSuperStruct()
    end
    return false
end

local function IsPatched(Object, PatchFunction)
    local ClassPath = PathOf(Object:GetClass())
    if not ClassPath then return false end
    if PatchedClass[ClassPath] == nil then
        PatchedClass[ClassPath] = ClassHasFunction(Object:GetClass(), PatchFunction)
        Log("Patch check " .. ClassPath .. ":" .. PatchFunction .. " -> " .. tostring(PatchedClass[ClassPath]))
        if not PatchedClass[ClassPath] and not WarnedUnpatched then
            WarnedUnpatched = true
            Log("Scripts are not patched (launch with -as-ignore-precompiled-data); menus stay unlocked and minigame "
                .. "discovery is off")
        end
    end
    return PatchedClass[ClassPath]
end

------------------------------------------------------------------------------------------------------------------------
-- Minigame discovery

local DiscoveredThisSession = {}

local function ApplyDiscovery(State)
    if not State then return end
    for _, Comp in ipairs(FindAllOf("MinigameComp") or {}) do
        if Comp:IsValid() and IsPatched(Comp, "HasArchipelagoPlayerInHudArea")
                and Comp.bArchipelagoPlayerInHudArea == true then
            local Id = Comp.MinigameID:ToString()
            if not DiscoveredThisSession[Id] then
                DiscoveredThisSession[Id] = true
                local Chapter = ChapterByMinigameId[Id]
                if Chapter then
                    SendCheck(Chapter.name .. " Discovered")
                else
                    Log("Discovered unknown minigame: " .. Id)
                end
            end
        end
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Menu locks: the patched pickers only show chapters and minigames set in these bitmasks.

-- Bit N = chapter database index N.
local function UnlockedChapterMask(State)
    if not State then return -1 end
    local Mask = 0
    for Name in pairs(State.Chapters) do
        Mask = Mask | (1 << ChapterByName[Name].index)
    end
    return Mask
end

-- Bit N = the Nth minigame.
local function DiscoveredMinigameMask(State)
    if not State then return -1 end
    local Mask = 0
    for Index, Minigame in ipairs(MinigameOrder) do
        if State.Minigames[Minigame.name] then
            Mask = Mask | (1 << (Index - 1))
        end
    end
    return Mask
end

local function ApplyMenuLocks(State)
    local ChapterMask = UnlockedChapterMask(State)
    for _, Picker in ipairs(FindAllOf("ChapterSelectPickerWidget") or {}) do
        if Picker:IsValid() then
            if IsPatched(Picker, "IsArchipelagoChapterUnlocked")
                    and Picker.ArchipelagoUnlockedChapters ~= ChapterMask then
                Picker.ArchipelagoUnlockedChapters = ChapterMask
            end
            PickerChapter = Picker.SelectedChapter.Name:ToString()
            PickerSeenTime = os.time()
        end
    end

    local MinigameMask = DiscoveredMinigameMask(State)
    for _, Picker in ipairs(FindAllOf("MinigamePickerWidget") or {}) do
        if Picker:IsValid() and IsPatched(Picker, "IsArchipelagoMinigameDiscovered")
                and Picker.ArchipelagoDiscoveredMinigames ~= MinigameMask then
            Picker.ArchipelagoDiscoveredMinigames = MinigameMask
        end
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Checkpoints

local ProgressManager = nil
local ProgressEventsRead = 0

local function ApplyProgressEvents(State)
    if not ProgressManager or not ProgressManager:IsValid() then
        ProgressManager = FindFirstOf("HazeAudioManager")
        ProgressEventsRead = 0
        if not ProgressManager or not ProgressManager:IsValid() then return end
    end
    if not IsPatched(ProgressManager, "IsArchipelagoProgressTracked") then return end

    local Events = ProgressManager.ArchipelagoProgressEvents
    local Count = Events:GetArrayNum()
    if Count < ProgressEventsRead then ProgressEventsRead = 0 end
    for Index = ProgressEventsRead + 1, Count do
        local Kind, Level, Name = Events[Index]:ToString():match("^(%a+)|(.-)|(.*)$")
        local Folder = Level and Level:match("^/Game/Maps/(.+)/[^/]+$")
        if Folder then
            local Key = Name .. " (" .. Folder .. ")"
            Log("Progress event: " .. Kind .. " " .. Key)
            StartSettle(Kind .. " " .. Key)
            if Kind == "saved" or Kind == "reached" then SendCheckpoint(State, Key) end
        end
    end
    ProgressEventsRead = Count
end

------------------------------------------------------------------------------------------------------------------------
-- Goal

local GoalSent = false

local function ApplyGoal(State)
    if not State or GoalSent then return end
    local Finished = 0
    for _, Comp in ipairs(FindAllOf("SmoochUserComponent") or {}) do
        if Comp:IsValid() and Comp.Progress >= 1.0 then
            Finished = Finished + 1
        end
    end
    if Finished >= 2 then
        GoalSent = true
        Log("Final kiss complete!")
        SendCheck(GoalLine)
    end
end

------------------------------------------------------------------------------------------------------------------------
-- Main loops (all on the game thread)

local function Tick()
    local Capabilities, Progress = Statics()
    if not Capabilities or not Progress then return end
    local State = ReadState()
    local PlayerList = Players()
    ApplyBlocks(State, PlayerList, Capabilities, false)
    ApplyProgress(State, PlayerList, Progress)
    ApplyProgressEvents(State)
    ApplyDiscovery(State)
    ApplyGoal(State)
end

local LastTickError = nil

LoopInGameThreadWithDelay(PollMs, function()
    local Ok, Err = pcall(Tick)
    local Message = (not Ok) and tostring(Err) or nil
    if Message and Message ~= LastTickError then Log("Tick failed: " .. Message) end
    if not Message and LastTickError then Log("Tick recovered") end
    LastTickError = Message
end)

local LastSettleError = nil
local WasSettling = false

LoopInGameThreadWithDelay(SettleMs, function()
    local Now = Settling()
    if WasSettling and not Now then Log("Locks settled") end
    WasSettling = Now
    if not Now then return end
    local Ok, Err = pcall(function()
        local Capabilities = Statics()
        if Capabilities then ApplyBlocks(ReadState(), Players(), Capabilities, true) end
    end)
    local Message = (not Ok) and tostring(Err) or nil
    if Message and Message ~= LastSettleError then Log("Settling locks failed: " .. Message) end
    LastSettleError = Message
end)

-- Faster loop so locked chapters disappear from the menu quickly.
local LastMenuError = nil

LoopInGameThreadWithDelay(MenuPollMs, function()
    local Ok, Err = pcall(function() ApplyMenuLocks(ReadState()) end)
    local Message = (not Ok) and tostring(Err) or nil
    if Message and Message ~= LastMenuError then Log("Menu lock failed: " .. Message) end
    if not Message and LastMenuError then Log("Menu lock recovered") end
    LastMenuError = Message
end)

Log("Loaded. Bridge folder: " .. BridgeDir)
