import string
import re
import collections
import configparser
import tuxmodifier
import sys


configtarget = ["CPU", "sensors", "river", "Kernel"]
bodypart= {}
bodypart['head'] = 0
head = ['head_skin','smile','right_eyelid','shadow_under_beak', 'right_eyebrows', 'left_eyebrows', 'left_pupil','left_pupil_reflection', 'beak_bottom_part', 'beak_bottom_part_reflection','beak_upper_part', 'beak_upper_part_reflection', 'right_nostril']
bodypart['left_arm'] = 0
left_arm = ['left_arm', 'left_arm_reflection', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm', 'left_palm_reflection']
bodypart['right_arm'] = 0
right_arm = ['right_arm', 'right_arm_reflection','right_arm_shadow_1', 'right_arm_shadow_2', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2','right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection']
bodypart['body'] = 0
body = ['skin', 'right_leg', 'left_leg', 'belly', 'torso_shadow',  'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow', 'neck_reflection','skin_reflection', 'unknown_part' ]
# 'left_nostril', 'beak_right_end', 'left_eyelid','white_left_eye', 'white_right_eye', 'beak_shadow_on_eyes', 'skin_between_eyes', 'forehead_reflection', 'right_pupil', 'right_pupil_reflection_1','right_pupil_reflection_2'

#bodypart['left_eye'] = 0
#left_eye = ['white_left_eye', 'left_pupil', 'left_pupil_reflection', 'left_eyelid']
#bodypart['right_eye'] = 0
#right_eye = ['white_right_eye', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid']
#bodypart['beak'] = 0
#beak = ['beak_bottom_part', 'beak_bottom_part_reflection', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end']
#bodypart['head'] = 0
#head = ['']
#bodypart['body'] = 0
#body = ['skin', 'right_leg', 'left_leg', 'head_skin', 'skin_between_eyes', 'forehead_reflection', 'right_eyebrows', 'left_eyebrows', 'right_arm', 'right_arm_reflection', 'neck_reflection', 'skin_reflection', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection']
#bodypart['torso'] = 0
#torso = ['belly', 'torso_shadow', 'shadow_under_beak', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow']
#bodypart['left_palm'] = 0
#left_palm = ['left_palm', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm_reflection']
#bodypart['right_palm'] = 0
#right_palm = ['right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection', 'right_arm_shadow_1', 'right_arm_shadow_2']
#not used : beak_shadow_on_eyes, smile,



def main():
    if sys.argv[1]:
        filename = sys.argv[1]
    tuxmodifier.reinit()
    configparser.filldic(filename)

    gc = configparser.globalcontainer

    # for key in gc:
    #     if "CPU" in key:
    #         bodypart['head'] += configparser.hexformat(key)
    #     elif "sensors" in key:
    #         bodypart['left_arm'] += configparser.hexformat(key)
    #     elif "river" in key:
    #         bodypart['right_arm'] += configparser.hexformat(key)
    #     elif "Kernel" in key:
    #         bodypart['body'] += configparser.hexformat(key)



    for key in bodypart:

        if "head" in key:
            for zone in head:
                tuxmodifier.modify(configparser.hexformat('CPU'), zone)
        elif "left_arm" in key:
            for zone in left_arm:
                tuxmodifier.modify(configparser.hexformat('sensors'), zone)
        elif "right_arm" in key:
            for zone in right_arm:
                tuxmodifier.modify(configparser.hexformat('river'), zone)
        elif "body" in key :
            for zone in body:
                tuxmodifier.modify(configparser.hexformat('Kernel'), zone)



if __name__=="__main__":
    main()
