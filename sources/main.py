import string
import re
import collections
import configparser
import tuxmodifier
import colorengine
import sys


#
# Declaration of the different body part of the tux
#
bodypart = ['head','beak','left_eye','right_eye','body','torso','left_palm','right_palm']

head = ['skin_between_eyes', 'head_skin', 'forehead_reflection', 'right_eyebrows', 'left_eyebrows', ]
beak = ['smile', 'beak_shadow_on_eyes', 'beak_bottom_part', 'beak_bottom_part_reflection', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end']
left_eye = ['white_left_eye', 'left_pupil', 'left_pupil_reflection', 'left_eyelid']
right_eye = ['white_right_eye', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid']
body = ['skin', 'right_leg', 'left_leg', 'right_arm', 'right_arm_reflection', 'neck_reflection', 'skin_reflection', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection']
torso = ['belly', 'torso_shadow', 'shadow_under_beak', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow']
left_palm = ['left_palm', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm_reflection']
right_palm = ['right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection', 'right_arm_shadow_1', 'right_arm_shadow_2'] # enlever :




def main():
    # If you choose to put your own .config file
    if sys.argv[1]:
        filename = sys.argv[1]

    tuxmodifier.reinit()

    # Fill globalcontainer with all options
    # key: name of the menu, value: configuration with value(y,m,n)
    configparser.filldic(filename)

    # gc is now the dictionnary
    gc = configparser.globalcontainer


    # Select the different part to modify
    # Each body part is assigned to a key word in gc
    for key in bodypart:

        if "left_eye" in key:
            color1 = colorengine.hexformat('sensors')
            color2 = colorengine.modifycolor(color1,-50)
            reflection = colorengine.reflectioncolor(color1)
            for zone in left_eye:
                if 'left_pupil' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'white' in zone:
                    tuxmodifier.modify(reflection, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "right_eye" in key:
            color1 = colorengine.hexformat('Net')
            color2 = colorengine.modifycolor(color1,-50)
            color3 = colorengine.modifycolor(color1,50)
            reflection = colorengine.reflectioncolor(color1)
            for zone in right_eye:
                if 'right_pupil' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'reflection' or 'white' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'eyelid' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "beak" in key:
            color1 = colorengine.hexformat('river')
            color2 = colorengine.modifycolor(color1,20)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color1)
            for zone in beak:
                if 'nostril' in zone:
                    tuxmodifier.modify(colorengine.hexformat('Kernel'), zone)
                elif 'smile' in zone:
                    tuxmodifier.modify(colorengine.hexformat('Kernel'), zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'shadow' in zone:
                    tuxmodifier.modify(shadow, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "head" in key:
            color1 = colorengine.hexformat('system')
            color2 = colorengine.modifycolor(color1,-50)
            color3 = colorengine.modifycolor(color1,30)
            reflection = colorengine.reflectioncolor(color1)
            for zone in head:
                if 'reflection' in zone:
                    tuxmodifier.modify(reflection, zone)
                elif 'eyebrows' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'eyes' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
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
            color1 = colorengine.hexformat('devices')
            color2 = colorengine.modifycolor(color1, 100)
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



        tuxmodifier.addaccessory("sprays/hat.png","tux_mod.svg",70,-30)


if __name__=="__main__":
    main()
