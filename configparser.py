import string
import re

#globalcontainer : dictionnary holding pairs {'Configuration menu' : 'list of configurations'}
#contents : intermediary value holding .config file content in plain text
globalcontainer = {}
contents = ""

#Initialize global variables
def initdic():
    global globalcontainer
    global contents
    globalcontainer = {key : [] for key in range(512)}
    contents = ""
    #print("New dictionnary with empty lists has been created : " + str(globalcontainer) + "\n")

#Returns the number of all configurations in the .config file
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

#Checks if the argument configuration is currently active in this .config file
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
    counter = 0
    if symbol=='y' or symbol=='m':
        for key in globalcontainer:
            if configmenu in key:
                for item in globalcontainer[key]:
                    if item[-1:] == symbol:
                        counter += 1
        if counter == 1:
            print("%d configuration set to \'%s\' has been found in \"%s\"...\n" % (counter, symbol,configmenu))
        elif counter > 1:
            print("%d configurations set to \'%s\' have been found in \"%s\"...\n" % (counter, symbol,configmenu))
        else: print("No configurations set to \'%s\' have been found in \"%s\"...\n" % (symbol, configmenu))
        return counter
    else: print("Symbol is currently set to \'%s\' but allowed symbol must be either 'y' or 'm'" % symbol)

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
    #initdic()
    filldic("linux-4.13.3/.config")

    #res = findconfigcat("CONFIG_ARCH_HAS_SG_CHAIN")
    #res2 = isconfigenabled("CONFIG_ARCH_HAS_SG_CHAIN")
    #print(res2)
    #countconfig("y","Library routines")

    for x in globalcontainer:
        print(x)


if __name__=="__main__":
    main()
