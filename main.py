import string
import re
import collections
import configparser
import tuxmodifier
import sys

tabmod = [0,0,0,0,0,0,0,0,0,0]
configtarget = ["USB", "CPU", "Kernel", "sensors", "river"]

def main(filename = "linux-4.13.3/.config"):
    tuxmodifier.reinitColor()
    configparser.filldic(filename)

    gc = configparser.globalcontainer

    for key in gc:
        tabmod[0] += configparser.countconfig('y',key)
        tabmod[1] += configparser.countconfig('m',key)
    tabmod[2] = configparser.nbconfig() - tabmod[0] - tabmod[1]


    for key in range(0, len(configtarget)):
        tabmod[key+3]=configparser.countconfig('y',configtarget[key])




    print(tabmod)


if __name__=="__main__":
    main()
