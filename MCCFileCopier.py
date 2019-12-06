###########################################
#Author: GetParanoid
#Description: Simple python script that helps swapping your modded files and your vanilla files for MCC.
#Version: 1.5
###########################################
import time
import os
from findMCC import findMCC

# Check where MCC location is
steamdir = findMCC()
print(steamdir)

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
    if os.path.isdir(steamdir + ModFolder) & os.path.isdir(steamdir + ModFolder + VanillaFiles)  == 1:
        print("Directories = OK")
        if os.path.isfile(steamdir + VanillaPak) & os.path.isfile(steamdir + VanillaMap) & os.path.isfile(steamdir + ModPak) & os.path.isfile(steamdir + ModMap) == 1:
            print("Files in MODS folder = OK\n")
            userInput = input("ENTER [ 1 ] - Copy Vanilla Files \nENTER [ 2 ] - Copy Modded Files\nINPUT: ")
            if userInput == "1":
                os.system('cls')
                print("Syncing Vanilla Files to MCC")
                os.unlink(steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
                os.unlink(steamdir + targetMap + 'forge_halo.map')
                os.link(steamdir + VanillaPak, steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
                os.link(steamdir + VanillaMap, steamdir + targetMap + 'forge_halo.map')
                print("COMPLETE")
                os.system('pause')
            elif userInput == "2":
                os.system('cls')
                print("Syncing Modded Files to MCC")
                os.unlink(steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
                os.unlink(steamdir + targetMap + 'forge_halo.map')
                os.link(steamdir + ModPak, steamdir + targetPak + 'MCC-WindowsNoEditor.pak')
                os.link(steamdir + ModMap, steamdir + targetMap + 'forge_halo.map')
                print("COMPLETE")
                os.system('pause')
            else:
                os.system('cls')
                print("Invalid input")
                time.sleep(2)
                os.system('cls')
                copyFiles()
        else:
            print("Missing Files - Either Vanilla[or]Modded forge_halo.map or MCC-WindowsNoEditor.pak not found within MODS folder")
            os.system('pause')
    else:
        print("Improper File Structure, aborting.")
        os.system('pause')

copyFiles()


