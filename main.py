import string
import re
import collections
import configparser
import tuxmodifier
import sys

tabmod = [0,0,0,0,0,0,0,0,0,0]
configtarget = ["USB", "CPU", "Kernel", "sensors", "river"]
bodypart = ['skin', 'right_leg', 'left_leg', 'head_skin', 'belly', 'torso_shadow', 'shadow_under_beak', 'white_left_eye', 'white_right_eye', 'beak_shadow_on_eyes', 'skin_between_eyes', 'forehead_reflection', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid', 'right_eyebrows', 'left_eyebrows', 'left_pupil','left_pupil_reflection', 'beak_bottom_part', 'beak_bottom_part_reflection', 'smile', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end', 'left_eyelid', 'right_arm', 'right_arm_reflection', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow', 'neck_reflection', 'right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection', 'skin_reflection', 'unknown_part', 'right_arm_shadow_1', 'right_arm_shadow_2', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm', 'left_palm_reflection']

def main():
    if sys.argv[1]:
        filename = sys.argv[1]
    tuxmodifier.reinit()
    configparser.filldic(filename)

    gc = configparser.globalcontainer

    for key in gc:
        tabmod[0] += configparser.countconfig('y',key)
        tabmod[1] += configparser.countconfig('m',key)
    tabmod[2] = configparser.nbconfig() - tabmod[0] - tabmod[1]


    for key in range(0, len(configtarget)):
        tabmod[key+3]=configparser.countconfig('y',configtarget[key])

    tuxmodifier.modify('FF5300', bodypart[4])
    #for xrange in range(0, len(bodypart)):
    #    newhex = hex(tabmod[xrange])
    #    tuxmodifier.modify(newhex, bodypart[xrange])




    print(tabmod)


if __name__=="__main__":
    main()
