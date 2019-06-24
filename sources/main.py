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
    tuxmodifier.reinit()

    # Fill dictionnary with configuration file's values
    # key: name of the menu, value: configuration with value(y,m,n)
    configparser.filldic(filename)

<<<<<<< HEAD
    # gc is now the dictionnary
    gc = configparser.globalcontainer
    resizefactor = 0
    y=0
    m=0
    n=0
    for i in gc:
        y += configparser.countconfig("y",i)
        m += configparser.countconfig("m",i)
        n += configparser.countconfig("n",i)

    maincololor = '%02x%02x%02x' % (y%255,m%255,n%255)

    # Select the different part to modify
    # Each body part is assigned to a key word in gc
    for key in bodypart:

        if "left_eye" in key:
            color1 = colorengine.hexformat('system')
            color2 = colorengine.modifycolor(color1,-55)
            color3 = colorengine.modifycolor(color1,15)
            reflection = colorengine.reflectioncolor(color1)
            for zone in left_eye:
                if 'left_pupil' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(reflection,zone)
                elif 'white' in zone:
                    tuxmodifier.modify(reflection, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "right_eye" in key:
            color1 = colorengine.hexformat('system')
            color2 = colorengine.modifycolor(color1,-50)
            color3 = colorengine.modifycolor(color1,20)
            reflection = colorengine.reflectioncolor(color1)
            for zone in right_eye:
                if 'right_pupil' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(reflection,zone)
                elif 'white' in zone:
                    tuxmodifier.modify(reflection, zone)
                # elif 'eyelid' in zone:
                #     tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color3, zone)
        elif "beak" in key:
            color1 = colorengine.hexformat('river')
            color2 = colorengine.modifycolor(color1,-40)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color2)
            for zone in beak:
                if 'nostril' in zone:
                    tuxmodifier.modify(color1,zone)
                elif 'smile' in zone:
                    tuxmodifier.modify(colorengine.hexformat('Kernel'), zone)
                # elif 'reflection' in zone:
                #     tuxmodifier.modify(reflection, zone)
                elif 'shadow' in zone:
                    tuxmodifier.modify(shadow, zone)
                else:
                    tuxmodifier.modify(color2, zone)
        elif "head" in key:
            color1 = colorengine.hexformat('sensors')
            color2 = colorengine.modifycolor(color1,25)
            color3 = colorengine.shadowcolor(color2)
            reflection = colorengine.reflectioncolor(color1)
            for zone in head:
                if 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'eyebrows' in zone:
                    tuxmodifier.modify(color1, zone)
                elif 'eyes' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color2, zone)
        elif "body" in key:
            color1 = colorengine.hexformat('CPU')#Kernel
            color2 = colorengine.modifycolor(color1,20)
            color3 = colorengine.modifycolor(color1,20)
            shadow = colorengine.shadowcolor(color1)
            reflection = colorengine.reflectioncolor(color1)
            for zone in body:
                if 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                if 'leg' in zone:
                    tuxmodifier.modify(color3, zone)
                elif 'skin' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "torso" in key:
            color1 = colorengine.hexformat('Net')
            color2 = colorengine.modifycolor(color1,40)
            shadow = colorengine.shadowcolor(color1)
            for zone in torso:
                if 'shadow' in zone:
                    tuxmodifier.modify(shadow, zone)
                elif 'belly' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "left_palm" in key:
            color1 = colorengine.hexformat('USB')
            color2 = colorengine.modifycolor(color1,-50)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color1)
            for zone in left_palm:
                if 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'shadow_1' in zone:
                    tuxmodifier.modify(shadow, zone)
                elif 'shadow_2' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "right_palm" in key:
            color1 = colorengine.hexformat('support')
            color2 = colorengine.modifycolor(color1,20)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color1)
            for zone in right_palm:
                if 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'shadow_1' in zone:
                    tuxmodifier.modify(shadow, zone)
                elif 'shadow' in zone:
                    tuxmodifier.modify(reflection, zone)
                else:
                    tuxmodifier.modify(color1, zone)


=======
    # Painting time!
    tuxmodifier.tuxcolorizer()
>>>>>>> 0a2546525c884fce45a692647995f91a23e96dd0

    # Adding accessories
    tuxmodifier.accessoryhandler()

if __name__=="__main__":
    main()
