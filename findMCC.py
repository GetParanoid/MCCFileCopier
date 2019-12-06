import os
location = ''
def findDir(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            global location
            location = (os.path.join(root, name))
            location = os.path.dirname(os.path.realpath(location))
            return True
    return False

def findMCC():
    try:
        file = os.getcwd() + '\\location.txt'
        if os.stat(file).st_size == 0:
            raise Exception("Location file is empty")
        locationFile = open('location.txt', 'r')
        steamdir = locationFile.read()
        if not findDir('mcclauncher.exe', steamdir):
            raise Excpetion("MCC is located in wrong directory")
        locationFile.close()
        return steamdir
    except:
        locationFile = open('location.txt', 'w')
        # Find MCC Directory
        findSteam64 = "C:\\Program Files\\"
        findSteamx86 = "C:\\Program Files (x86)\\"
        steamdir = ''
        yes = ['y','ye','yes']
        uInput = input("Is Halo: MCC located in the default Steam location?")
        global location
        if uInput.lower() in yes:
            if findDir('mcclauncher.exe', findSteamx86):
                steamdir = location + '\\'
            elif findDir('mcclauncher.exe', findSteam64):
                steamdir = location + '\\'
            else:
                print('Halo: MCC not found')
        else:
            steamdir = input("Where is the directory containing Halo: MCC located?")
            if findDir('mcclauncher.exe', steamdir):
                steamdir = location + '\\'
            else:
                print("MCC directory not found")
        locationFile.write(steamdir)
        locationFile.close()
        for i in range(0,len(steamdir)):
            if steamdir[i] == '\\':
                steamdir[i] = '/'
        return steamdir
