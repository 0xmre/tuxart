import string
import re
import collections
import configparser
import tuxmodifier
import sys

configtarget = ["CPU", "sensors", "river", "Kernel"]
bodypart= {}
#bodypart['head'] = 0
#head = ['head_skin','smile','right_eyelid','shadow_under_beak', 'right_eyebrows', 'left_eyebrows', 'left_pupil','left_pupil_reflection', 'beak_bottom_part', 'beak_bottom_part_reflection','beak_upper_part', 'beak_upper_part_reflection', 'right_nostril']
#bodypart['left_arm'] = 0
#left_arm = ['left_arm', 'left_arm_reflection', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm', 'left_palm_reflection']
#bodypart['right_arm'] = 0
#right_arm = ['right_arm', 'right_arm_reflection','right_arm_shadow_1', 'right_arm_shadow_2', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2','right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection']
#bodypart['body'] = 0
#body = ['skin', 'right_leg', 'left_leg', 'belly', 'torso_shadow',  'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow', 'neck_reflection','skin_reflection', 'unknown_part' ]
# 'left_nostril', 'beak_right_end', 'left_eyelid','white_left_eye', 'white_right_eye', 'beak_shadow_on_eyes', 'skin_between_eyes', 'forehead_reflection', 'right_pupil', 'right_pupil_reflection_1','right_pupil_reflection_2'

bodypart['left_eye'] = 0
bodypart['right_eye'] = 0
bodypart['beak'] = 0
bodypart['head'] = 0
bodypart['body'] = 0
bodypart['torso'] = 0
bodypart['left_palm'] = 0
bodypart['right_palm'] = 0

left_eye = ['white_left_eye', 'left_pupil', 'left_pupil_reflection', 'left_eyelid']
right_eye = ['white_right_eye', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid']
beak = ['smile', 'beak_shadow_on_eyes', 'beak_bottom_part', 'beak_bottom_part_reflection', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end']
head = ['skin_between_eyes', 'head_skin', 'forehead_reflection', 'right_eyebrows', 'left_eyebrows', ]
body = ['skin', 'right_leg', 'left_leg', 'right_arm', 'right_arm_reflection', 'neck_reflection', 'skin_reflection', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection']
torso = ['belly', 'torso_shadow', 'shadow_under_beak', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow']
left_palm = ['left_palm', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm_reflection']
right_palm = ['right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection'] # enlever : , 'right_arm_shadow_1', 'right_arm_shadow_2'
#not used : beak_shadow_on_eyes, smile,



def main():
    if sys.argv[1]:
        filename = sys.argv[1]
    tuxmodifier.reinit()
    configparser.filldic(filename)

    gc = configparser.globalcontainer



    for key in bodypart:

        if "left_eye" in key:
            color1 = configparser.hexformat('sensors')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,50)
            for zone in left_eye:
                if 'left_pupil' in zone:
                    tuxmodifier.modify(color3, zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "right_eye" in key:
            color1 = configparser.hexformat('Net')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,50)
            for zone in right_eye:
                if 'right_pupil' in zone:
                    tuxmodifier.modify(color3, zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "beak" in key:
            color1 = configparser.hexformat('IPV')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,20)
            for zone in beak:
                if 'nostril' in zone:
                    tuxmodifier.modify(configparser.hexformat('CPU'), zone)
                elif 'smile' in zone:
                    tuxmodifier.modify(configparser.hexformat('CPU'), zone)
                elif 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'shadow' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "head" in key:
            color1 = configparser.hexformat('system')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,100)
            for zone in head:
                if 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'eyebrows' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "body" in key:
            color1 = configparser.hexformat('Kernel')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,20)
            for zone in body:
                if 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                if 'leg' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "torso" in key:
            color1 = configparser.hexformat('devices')
            color2 = configparser.lowercolor(color1,20)
            for zone in torso:
                if 'shadow' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "left_palm" in key:
            color1 = configparser.hexformat('USB')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,10)
            for zone in left_palm:
                if 'reflection' in zone:
                    tuxmodifier.modify(color2, zone)
                elif 'shadow' in zone:
                    tuxmodifier.modify(color3, zone)
                else:
                    tuxmodifier.modify(color1, zone)
        elif "right_palm" in key:
            color1 = configparser.hexformat('support')
            color2 = configparser.uppercolor(color1,20)
            color3 = configparser.lowercolor(color1,5)
            for zone in right_palm:
                if 'reflection' in zone:
                    tuxmodifier.modify(color3, zone)
                if 'shadow' in zone:
                    tuxmodifier.modify(color2, zone)
                else:
                    tuxmodifier.modify(color1, zone)


if __name__=="__main__":
    main()
