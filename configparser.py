import string
import re


#globalcontainer : dictionnary holding pairs {'Configuration menu' : 'list of configurations'}
#contents : intermediary value holding .config file content in plain text
globalcontainer = {}
contents = ""
n="is not set"


#Returns the number of configurations in the .config file
def nbconfig():
    global globalcontainer
    count=0
    for key, values in globalcontainer.items():
        count += len(values)

    return count

#Retrieving configuration list from "contents" variable and ordering them by menu names as keys and corresponding list of configurations as values
def filldic(filename = ".config"):
    global globalcontainer
    global contents

    with open(filename,'r') as file:
        contents = file.read()
        file.close()

    categories = re.split("\n\n",contents)

    for cat in categories:
        cat = re.split("\n", cat)
        globalcontainer[cat[1]]=[]
        for line in range(3,len(cat)):
            globalcontainer[cat[1]].append(cat[line])
    print("Dictionnary has been succesfully updated and now has %d configurations...\n" % nbconfig())

#Checks if the argument configuration is currently active in this .config file while in a loop  or handling single configurations
def isconfigactive(configname):
    if configname[:1] == '#':
        return False
    return True

#Same behaviour as previous method, but can be used for checking configuration value if not inside a loop
def isconfigenabled(configname):
    global globalcontainer
    for key, values in globalcontainer.items():
        for item in values:
            if configname == item[:-2] and (item[-1:] == 'y' or item[-1:] == 'm'):
                return True
    return False


#Returns number of configuration set to symbol for a given configuration menu
#Symbol values must be either 'y' or 'm'
def countconfig(symbol, configmenu):
    global globalcontainer
    global n
    counter = 0
    if symbol=='y' or symbol=='m' or symbol=='n':
        for key in globalcontainer:
            if configmenu in key:
                for item in globalcontainer[key]:
                    if item[-len(n):] == n:
                        counter += 1
                    if item[-1:] == symbol:
                        counter += 1
    return counter

def hexformat(configmenu):
    red = countconfig('y',configmenu)
    green = countconfig('m',configmenu)
    blue = countconfig('n',configmenu)
    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue > 255:
        blue = 255
    res = '%02x%02x%02x' % (red, green, blue)
    return res

#Given the name of a configuration its parent menu will be returned
def findconfigcat(configname):
    global globalcontainer
    for key, values in globalcontainer.items():
        for item in values:
            if configname == item[:-2] and isconfigactive(item):
                print("Positive match! %s has been found in \"%s\" menu...\n" % (configname, key))
            elif configname in item and isconfigactive(item):
                print("Similar configurations such as %s has been in found in \"%s\" menu...\n" % (item[:-2], key))



def main():
    filldic("linux-4.13.3/.config")

    #res = findconfigcat("CONFIG_ARCH_HAS_SG_CHAIN")
    #res2 = isconfigenabled("CONFIG_ARCH_HAS_SG_CHAIN")
    #print(res2)
    #countconfig("y","Library routines")

    for x in globalcontainer:
        print(x)


if __name__=="__main__":
    main()
