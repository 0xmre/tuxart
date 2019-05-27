import string
import re

globalcontainer = {}
with open('.config','r') as file:
    contents = file.read()
    file.close()

def contentsplit():
    categories = re.split("\n\n",contents)

    for cat in categories:
        cat = re.split("\n", cat)
        globalcontainer[cat[1]]=[]
        for line in range(3,len(cat)):
            globalcontainer[cat[1]].append(cat[line])

def main():
    contentsplit()
    x = globalcontainer.get("# Library routines")

if __name__=="__main__":
    main()
