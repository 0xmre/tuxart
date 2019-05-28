import string
import re
import collections
import configparser
import tuxmodifier

tabmod = [0,0,0,0,0,0,0,0,0,0]

def main(filename = ".config"):
    tuxmodifier.reinitColor()
    configparser.filldic(filename)
    configparser.contentsplit()

    gc = configparser.globalcontainer

    for key in gc:
        tabmod[0] += configparser.countconfig('y',key)
        tabmod[1] += configparser.countconfig('m',key)
    tabmod[2] = len(gc) - tabmod[0] - tabmod[1]


    print(tabmod)


if __name__=="__main__":
    main()
