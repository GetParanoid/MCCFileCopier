#####################v######################
#Author: GetParanoid
#Description: Simple python script that helps swapping your modded files and your vanilla files for MCC.
#Version: 1.1
###########################################

import time
import os
import shutil
#Get Steam Directory
steamdir = "C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/"

#Get Modded file directory(Using steamdir as base directory)
ModPak = 'MODS/MCC-WindowsNoEditor.pak'
ModMap = 'MODS/forge_halo.map'
#Get Vanilla Files Directory(Using steamdir as base directory)
VanillaPak = 'MODS/Vanilla Files/MCC-WindowsNoEditor.pak'
VanillaMap = 'MODS/Vanilla Files/forge_halo.map'

#Get MCC file locations for mods and maps
targetPak = 'MCC/Content/Paks'
targetMap = 'haloreach/maps'

def copyFiles():
    print("Made by reddit.com/u/GetParanoid - Contact for any issues and/or ideas\n")
    userInput = input("ENTER [ 1 ] - Copy Vanilla Files \nENTER [ 2 ] - Copy Modded Files\nINPUT: ")
    os.system('cls')
    if userInput == "1":
        print("Copying Vanilla Files to MCC")
        shutil.copy(os.path.join(steamdir + VanillaPak), os.path.join(steamdir + targetPak, 'MCC-WindowsNoEditor.pak'))
        shutil.copy(os.path.join(steamdir + VanillaMap), os.path.join(steamdir + targetMap, 'forge_halo.map'))
        print("COMPLETE")
        os.system('pause')
    elif userInput == "2":
        print("Copying Modded Files to MCC")
        shutil.copy(os.path.join(steamdir + ModPak), os.path.join(steamdir + targetPak, 'MCC-WindowsNoEditor.pak'))
        shutil.copy(os.path.join(steamdir + ModMap), os.path.join(steamdir + targetMap, 'forge_halo.map'))
        print("COMPLETE")
        os.system('pause')
    else:
        print("Invalid input")
        time.sleep(2)
        os.system('cls')
        copyFiles()

copyFiles()


