# Buckshot Roulette Archipelago Setup Guide

## Requirements

- Buckshot Roulette (Steam v2.2.0)
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases)

## Installation

- [Windows](#windows)
- [Linux](#linux)

---

### Windows
1.  Download and extract the mod loader (`gml-7.0.1-custom.zip`) [HERE](https://github.com/asdfwyay/APBuckshot-Client/releases/tag/gml-7.0.1-custom).
   
2.  Navigate to the Buckshot Roulette game folder.
    > It is typically located at the following directory, which you can copy and paste into File Explorer.
    > ```cmd
    > `C:\Program Files (x86)\Steam\steamapps\common\Buckshot Roulette\Buckshot Roulette_windows`
    > ```
    > 
    > You can also find it through Steam by following the steps below:
    > 1. Right-click `Buckshot Roulette` in the left sidebar.
    > 2. Click `Properties`.
    > 3. In the new window, click `Installed Files` in the left sidebar.
    > 4. Click `Browse...`. Your file manager should appear.
    > 5. Open `Buckshot Roulette_{windows}`.
    > 6. You should now be able to see `Buckshot Roulette.exe`.

3.  Place the `/addons` folder from the mod loader into the `Buckshot Roulette_windows` folder.

4.  Install the mod loader using **ONE** of the methods listed below.
   
    #### Shortcut
    1. Right-click `Buckshot Roulette.exe`, then click `Create shortcut`.
       
    2. Right-click the shortcut you created (typically named `Buckshot Roulette.exe - Shortcut`).
    then click `Properties`.

    3. Add the following to the end of the `Target` field:
    
    ```cmd
     --script addons/mod_loader/mod_loader_setup.gd
    ```
    
    4. Run the shortcut.

    #### Powershell
    Replace `<path/to/game/dir>` with the path to the `Buckshot Roulette_windows` folder.
    ```pwsh
    cd "<path/to/game/dir>"
    & ".\Buckshot Roulette.exe" --script addons/mod_loader/mod_loader_setup.gd
    ```

    #### Command Prompt
    Replace `<path/to/game/dir>` with the path to the `Buckshot Roulette_windows` folder.
    ```cmd
    cd "<path/to/game/dir>"
    ".\Buckshot Roulette.exe" --script addons/mod_loader/mod_loader_setup.gd
    ```

5.  Wait for Godot Mod Loader to finish its installation. You will receive a prompt to restart
the game once this happens. After completion, you should see two executables in the installation folder:
    - `Buckshot Roulette.exe`
    - `Buckshot Roulette-vanilla.exe`

6.  Create a `/mods` directory in your installation folder and move the Buckshot Roulette Archipelago mod (`asdfwyay-APBuckshot-{version}.zip`) there. **Do not unzip the mod.**

7.  Create a shortcut of `Buckshot Roulette.exe` and move it to an accessible location on your PC. You can use this shortcut to run the modded version.
    > If you made a shortcut during Step 4, you can use the same shortcut,
    > but remove ` --script addons/mod_loader/mod_loader_setup.gd` from the
    > end of the `Target` field.

    Alternatively, add the modded executable to your Steam library:
    1. Click `Add a Game` at the bottom left.
    2. Click `Add a Non-Steam Game...`.
    3. On the window that opens, click `Browse...` on the bottom left.
    4. Navigate to `Buckshot Roulette.exe`, select it, and click `Open`.
    5. Click `Add Selected Programs`. You can now launch the modded version through Steam.
    6. **Optional**: Rename the modded shortcut to something more easily disinguishable (e.g. `Buckshot Roulette Archipelago`)

8.  Launch Buckshot Roulette and enjoy! A notification will appear on your first launch stating
that new mods have been installed. When reaching the start menu, an `ARCHIPELAGO` button should be visible
below the `MULTIPLAYER` button.

---

### Linux
1.  Download and extract the mod loader (`gml-7.0.1-custom.zip`) [HERE](https://github.com/asdfwyay/APBuckshot-Client/releases/tag/gml-7.0.1-custom).
   
2.  Navigate to the Buckshot Roulette game folder.
    > You can find it through Steam by following the steps below:
    > 1. Right-click `Buckshot Roulette` in the left sidebar.
    > 2. Click `Properties`.
    > 3. In the new window, click `Installed Files` in the left sidebar.
    > 4. Click `Browse...`. Your file manager should appear.
    > 5. Open `Buckshot Roulette_linux`.
    > 6. You should now be able to see `Buckshot Roulette.x86_64`.

3.  Place the `/addons` folder from the mod loader into the `Buckshot Roulette_linux` folder.

4.  Install the mod loader. Replace `<path/to/game/dir>` with the path to the `Buckshot Roulette_linux` folder.
    ```sh
    cd "<path/to/game/dir>"
    ./"Buckshot Roulette.x86_64" --script addons/mod_loader/mod_loader_setup.gd --setup-create-override-cfg
    ```

5.  Wait for Godot Mod Loader to finish its installation. You will receive a prompt to restart
the game once this happens. After completion, you should now see `override.cfg` in your
installation folder along with `Buckshot Roulette.x86_64`.

6.  Create a `/mods` directory in your installation folder and move the Buckshot Roulette Archipelago mod (`asdfwyay-APBuckshot-{version}.zip`) there. **Do not unzip the mod.**

7.  Add the modded executable to your Steam library:
    1. Click `Add a Game` at the bottom left.
    2. Click `Add a Non-Steam Game...`.
    3. On the window that opens, click `Browse...` on the bottom left.
    4. Open `Buckshot Roulette.x86-64`. You may need to set the file type to `All Files` in your file manager when looking for it.
    5. Click `Add Selected Programs`. You can now launch the modded version through Steam.
    6. **Optional**: Rename the modded shortcut to something more easily disinguishable (e.g. `Buckshot Roulette Archipelago`)

8.  Launch Buckshot Roulette and enjoy! A notification will appear on your first launch stating
that new mods have been installed. When reaching the start menu, an `ARCHIPELAGO` button should be visible
below the `MULTIPLAYER` button.
    > If you experience crashes or graphical issues when starting the game, add the following to the game's launch options:
    > ```sh
    > --rendering-driver opengl3
    > ```

## Updating

1.  Navigate to the `/mods` directory in your Buckshot Roulette installation folder.
2.  Replace the old mod ZIP with the new one (`asdfwyay-APBuckshot-{version}.zip`).
3.  Delete `mod-hooks.zip` in your installation folder if it exists.
4.  Launch Buckshot Roulette and enjoy! A notification will appear upon launching stating
that new mods have been installed.

## Connecting to a Game

1.  From the main menu, click `ARCHIPELAGO`. A menu should appear in the top left.
2.  Enter your slot name, server address, port, and password if needed.
3.  Click `CONNECT`.
4.  Wait until the status label in the menu updates to `CONNECTED`.
5.  Close the menu by clicking `CLOSE`.
6.  When ready, start playing by clicking `START`.
