# MCCFileCopier

https://reddit.com/r/halomods/comments/e6htyd/i_made_a_simple_python_script_to_automatically/


Prerequisites:

1. Install Python3
2. Create a folder inside your steam MCC installation folder called "MODS" 
3. Create a folder inside your MODS folder called "Vanilla Files"
4. Put your Modded forge_halo.map and MCC-WindowsNoEditor.pak inside the "MODS" folder
5. Put a copy of the Vanilla forge_halo.map and MCC-WindowsNoEditor.pak inside the "Vanilla Files" folder

How to Use:

1. Extract MCCFileCopier.py to your desktop / wherever you want
2. Launch MCCFileCopier.py
3. When asked for MCC install location, type YES if it's on your C: drive, type NO if it's on another drive and paste in the location
3. Enter 1 or 2 (1 - Copies Vanilla Files, 2 - Copies Modded Files)
4. Hit Enter

# How to add a new mod

1. Open MCCFileCopier.py in a text edior of you choice (Recommended: NotePad++ or VSCODE)
2. Find # HOW TO ADD A MOD(Line #24), follow these instructions
3. Add the mod's class to modList = [ ]
