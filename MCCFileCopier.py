import time
import os
import shutil

ModPak = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/MODS/MCC-WindowsNoEditor.pak'
ModMap = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/MODS/forge_halo.map'
VanillaPak = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/MODS/Vanilla Files/MCC-WindowsNoEditor.pak'
VanillaMap = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/MODS\Vanilla Files/forge_halo.map'

targetPak = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/MCC/Content/Paks'
targetMap = 'C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/haloreach/maps'

def copyFiles():
    print("Made by reddit.com/u/GetParanoid - Contact for any issues and/or ideas\n")
    userInput = input("ENTER [ 1 ] - Copy Vanilla Files \nENTER [ 2 ] - Copy Modded Files\nINPUT: ")
    os.system('cls')
    if userInput == "1":
        print("Copying Vanilla Files to MCC")
        shutil.copy(os.path.join(VanillaPak), os.path.join(targetPak, 'MCC-WindowsNoEditor.pak'))
        shutil.copy(os.path.join(VanillaMap), os.path.join(targetMap, 'forge_halo.map'))
        print("COMPLETE")
        os.system('pause')
    elif userInput == "2":
        print("Copying Modded Files to MCC")
        shutil.copy(os.path.join(ModPak), os.path.join(targetPak, 'MCC-WindowsNoEditor.pak'))
        shutil.copy(os.path.join(ModMap), os.path.join(targetMap, 'forge_halo.map'))
        print("COMPLETE")
        os.system('pause')
    else:
        print("Invalid input")
        time.sleep(2)
        os.system('cls')
        copyFiles()

copyFiles()


