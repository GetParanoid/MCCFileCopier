###########################################
#Author: GetParanoid
#Contributors: https://github.com/pbustos97 (findMCC.py), https://github.com/Ryan2537 (Complete restructure for easier mod adding)
#Description: Simple python script that helps swapping your modded files and your vanilla files for MCC.
#Version: 2.1
###########################################
import time
import os
from findMCC import findMCC

# Check where MCC location is
steamdir = findMCC()
print('\nMCC Install Location: ' + steamdir + "\n")


#Get Modded file directory(Using steamdir as base directory)
ModFolder = '/MODS'

#Get Vanilla Files Directory(Using steamdir as base directory)
VanillaFiles = ModFolder + "/Vanilla Files"




# HOW TO ADD A MOD
#Example Mod Below Copy/Paste to add a new one
class ModName():                            #create a class with the Mod's name
    fileName = 'MCC-WindowsNoEditor.pak'    #(Name of the mod's file)
    target = 'MCC/Content/Paks/'            #(The mod's install location inside MCC)
        # IMPORTANT : IF the mod has multiple files, add a new class for each file

#create an object for each mod
class EnableForgePak():
    fileName = 'MCC-WindowsNoEditor.pak'
    target = 'MCC/Content/Paks/'
class ForgeMap():
    fileName = 'forge_halo.map'
    target = 'haloreach/maps/'
class UnearthedDLL():
    fileName = 'haloreach.dll'
    target = 'haloreach/'
class UnearthedMap():
    fileName = 'cex_prisoner.map'
    target = 'haloreach/maps/'

#make a list of all mods you want to install / uninstall
#Add mod to the following list(Do NOT enable conflicting mods ex: same fileName)
modList = [ForgeMap, EnableForgePak]

def verifyFiles():
    if not os.path.isdir(steamdir + ModFolder):
        print('MODS folder not found')
        return False
    if not os.path.isdir(steamdir + VanillaFiles):
        print('Vanilla Files folder not found')
        return False
    for mod in modList:
        if not os.path.isfile(steamdir + ModFolder + '/' + mod.fileName):
            print(mod.fileName + ' not found in MODS folder')
            return False
        if not os.path.isfile(steamdir + VanillaFiles + '/' + mod.fileName):
            print(mod.fileName + ' not found in Vanilla Files folder')
            return False
    print("Files in MODS folder = OK")
    return True

def unlinkFiles(mod):
    os.unlink(steamdir + mod.target + mod.fileName)

def linkFiles(mod, modded):
    if (modded):
        os.link(steamdir + ModFolder + '/' + mod.fileName, steamdir + mod.target + mod.fileName)
    else:
        os.link(steamdir + VanillaFiles + '/' + mod.fileName, steamdir + mod.target + mod.fileName)

def copyFiles():
    print("Made by reddit.com/u/GetParanoid - Contact for any issues and/or ideas\n")
    if (verifyFiles()):
        userInput = input("ENTER [ 1 ] - Copy Vanilla Files \nENTER [ 2 ] - Copy Modded Files\nINPUT: ")
        if userInput == "1":
            os.system('cls')
            print("Syncing Vanilla Files to MCC")
            for mod in modList:
                unlinkFiles(mod)
                linkFiles(mod, False)
            print("COMPLETE")
            os.system('pause')
        elif userInput == "2":
            os.system('cls')
            print("Syncing Modded Files to MCC")
            for mod in modList:
                unlinkFiles(mod)
                linkFiles(mod, True)
            print("COMPLETE")
            os.system('pause')
        else:
            os.system('cls')
            print("Invalid input")
            time.sleep(2)
            os.system('cls')
            copyFiles()
    else:
        os.system('pause')

copyFiles()
