###########################################
#Author: GetParanoid
#Contributors: https://github.com/pbustos97 (findMCC.py), https://github.com/Ryan2537 (Complete restructure for easier mod adding)
#Description: Simple python script that helps swapping your modded files and your vanilla files for MCC.
#Version: 2.2
###########################################
import time
import os
import shutil
from findMCC import findMCC

# Check where MCC location is
steamdir = findMCC()
print('\nMCC Install Location: ' + steamdir + "\n")


#Get Modded file directory(Using steamdir as base directory)
ModFolder = '/MODS'

#Get Vanilla Files Directory(Using steamdir as base directory)
VanillaFiles = ModFolder + "/Vanilla Files"

#make a template for mods
class Mod():
    def __init__(self, fileName, target):
        self.fileName = fileName
        self.target = target

#to add a mod just follow the template [NAME] = Mod([FILENAME], [TARGETLOCATION])
#then add your mod to modList

#create an instance for each mod
forge = Mod('MCC-WindowsNoEditor.pak', 'MCC/Content/Paks/')
forgeMap = Mod('forge_halo.map', 'haloreach/maps/')

#make a list of all mods
modList = [forge, forgeMap]

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
        if not os.path.isfile(steamdir + mod.target + mod.fileName):
            print(mod.fileName + ' not found in game files')
            return False
        if not os.path.isfile(steamdir + VanillaFiles + '/' + mod.fileName):
            print(mod.fileName + ' not found in Vanilla Files\nCopying to Vanilla files')
            shutil.copyfile(steamdir + mod.target + mod.fileName, steamdir + VanillaFiles + '/' + mod.fileName)
    print("Files in MODS folder = OK\n")
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
