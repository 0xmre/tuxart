import string
import re
import collections
import configparser
import tuxmodifier
import sys

def main():
    
    # If you choose to put your own .config file
    if sys.argv[1]:
        filename = sys.argv[1]

    # Initialize tux_mod.svg
    tuxmodifier.tuxinit()

    # Fill dictionnary with configuration file's values
    # key: name of the menuconfig, value: configuration with value(y,m,n)
    configparser.filldic(filename)

    # Painting time!
    tuxmodifier.tuxcolorizer()

    # Adding accessories
    tuxmodifier.accessoryhandler()

if __name__=="__main__":
    main()
