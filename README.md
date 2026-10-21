# It Takes Two AP
Archipelago client implementation for It Takes Two.

## Requirements

- It Takes Two (Steam)
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) 0.6.7 or newer
- From this mod's release:
  - `ItTakesTwo-Archipelago-Installer.exe`
  - `it_takes_two.apworld`

## Setup Guide

### 1. Install the mod

1. Run `ItTakesTwo-Archipelago-Installer.exe` and allow it to make changes when Windows asks.
2. The installer finds the game through Steam. If it can't, drag the game folder into its window and press Enter.
   (In Steam: right-click It Takes Two > Manage > Browse local files.)
3. Press Enter to install.

No game files are replaced. To update the mod, run the new installer the same way. To remove it, run the installer and
press `U`.

### 2. Install the apworld

Double-click `it_takes_two.apworld` to add it to Archipelago, or copy it into the `custom_worlds` folder of your Archipelago install.

### 3. Generating
- To generate a game, follow [the official instructions.](https://archipelago.gg/tutorial/Archipelago/setup/en#generating-a-game)

### 4. Connecting

1. Open the Archipelago Launcher and click **It Takes Two Client**.
2. Enter the server address (for example `archipelago.gg:12345`) and connect with your slot name.
3. Start It Takes Two through Steam as normal.

## Credits

- [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) (MIT license) runs the mod's Lua scripts. The installer bundles
  UE4SS experimental build v3.0.1-1175 unmodified, with its license, plus this mod's config for It Takes Two
  (`ITTArchipelagoMod/ue4ss/config`).