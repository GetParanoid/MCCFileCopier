###########################################
#Author: GetParanoid
#Description: Simple python script that helps swapping your modded files and your vanilla files for MCC.
#Version: 1.3
###########################################
import time
import os
import shutil
#Get Steam Directory
steamdir = "C:/Program Files (x86)/Steam/steamapps/common/Halo The Master Chief Collection/"

#Get Modded file directory(Using steamdir as base directory)
ModFolder = 'MODS'
ModPak = ModFolder + '/MCC-WindowsNoEditor.pak'

ModMap = ModFolder + '/forge_halo.map'
#Get Vanilla Files Directory(Using steamdir as base directory)
VanillaFiles = "/Vanilla Files"
VanillaPak = ModFolder + '/Vanilla Files/MCC-WindowsNoEditor.pak'
VanillaMap = ModFolder +'/Vanilla Files/forge_halo.map'

#Get MCC file locations for mods and maps
targetPak = 'MCC/Content/Paks/'
targetMap = 'haloreach/maps/'

def copyFiles():
    print("Made by reddit.com/u/GetParanoid - Contact for any issues and/or ideas\n")
    userInput = input("ENTER [ 1 ] - Copy Vanilla Files \nENTER [ 2 ] - Copy Modded Files\nINPUT: ")
    if os.path.isdir(steamdir + ModFolder) & os.path.isdir(steamdir + ModFolder + VanillaFiles)  == 1:
        os.system('cls')
        if userInput == "1":
            print("Copying Vanilla Files to MCC")
            os.unlink(steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
            os.unlink(steamdir + targetMap + 'forge_halo.map')
            os.link(steamdir + VanillaPak, steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
            os.link(steamdir + VanillaMap, steamdir + targetMap + 'forge_halo.map')
            print("COMPLETE")
            os.system('pause')
        elif userInput == "2":
            print("Copying Modded Files to MCC")
            os.unlink(steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
            os.unlink(steamdir + targetMap + 'forge_halo.map')
            os.link(steamdir + ModPak, steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
            os.link(steamdir + ModMap, steamdir + targetMap + 'forge_halo.map')
            print("COMPLETE")
            os.system('pause')
        else:
            print("Invalid input")
            time.sleep(2)
            os.system('cls')
            copyFiles()
    else:
        print("Improper File Structure, aborting.")
        os.system('pause')

copyFiles()


