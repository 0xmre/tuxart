from xml.dom.minidom import parse
import xml.dom.minidom
import re
import xml.sax
import xml.dom
import colorengine
import configparser

import os


# Path to local files
path = os.path.dirname(os.path.realpath(__file__))
home = os.path.expanduser("~")
pathtomod = os.path.join(home,"Pictures/tux_mod.svg")


#
# Declaration of the different body part of the tux
#
bodypart = ['head','beak','left_eye','right_eye','body','torso','left_palm','right_palm']

# These arrays are fill with the different part of the tux to modify
head = ['skin_between_eyes', 'head_skin', 'forehead_reflection', 'right_eyebrows', 'left_eyebrows', ]
beak = ['smile', 'beak_shadow_on_eyes', 'beak_bottom_part', 'beak_bottom_part_reflection', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end']
left_eye = ['white_left_eye', 'left_pupil', 'left_pupil_reflection', 'left_eyelid']
right_eye = ['white_right_eye', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid']
body = ['skin', 'right_leg', 'left_leg', 'right_arm', 'right_arm_reflection', 'neck_reflection', 'skin_reflection', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection']
torso = ['belly', 'torso_shadow', 'shadow_under_beak', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow']
left_palm = ['left_palm', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm_reflection']
right_palm = ['right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection', 'right_arm_shadow_1', 'right_arm_shadow_2']

# Accesory adder
def accessoryhandler():
    # index in both lists links an item with a configuration
    configs = ["CONFIG_FTRACE","CONFIG_CPU_FREQ_DEFAULT_GOV_USERSPACE","CONFIG_CPU_FREQ_DEFAULT_GOV_PERFORMANCE","CONFIG_CPU_FREQ_DEFAULT_GOV_CONSERVATIVE","CONFIG_ENCRYPTED_KEYS","CONFIG_USB_USBNET"]
    items = ["eyepatch","helmet1","helmet2","helmet3","shield","cape"]

    for config, item in zip(configs,items):
        if configparser.isconfigenabled(config):
            addaccessory(item)

# Color every part of the tux
def tuxcolorizer():
    for key in bodypart:
        if "left_eye" in key:
            color1 = colorengine.hexformat('system')
            color2 = colorengine.modifycolor(color1,-30)
            color3 = colorengine.modifycolor(color1,10)
            reflection = colorengine.reflectioncolor(color1)
            for zone in left_eye:
                if 'left_pupil' in zone:
                    modify(color2, zone)
                elif 'reflection' in zone:
                    modify(reflection,zone)
                elif 'white' in zone:
                    modify(reflection, zone)
                else:
                    modify(color1, zone)
        elif "right_eye" in key:
            color1 = colorengine.hexformat('system')
            color2 = colorengine.modifycolor(color1,-30)
            color3 = colorengine.modifycolor(color1,10)
            reflection = colorengine.reflectioncolor(color1)
            for zone in right_eye:
                if 'right_pupil' in zone:
                    modify(color2, zone)
                elif 'reflection' in zone:
                    modify(reflection,zone)
                elif 'white' in zone:
                    modify(reflection, zone)
                else:
                    modify(color1, zone)
        elif "beak" in key:
            color1 = colorengine.hexformat('river')
            color2 = colorengine.modifycolor(color1,-40)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color2)
            for zone in beak:
                if 'nostril' in zone:
                    modify(color1,zone)
                elif 'smile' in zone:
                    modify(colorengine.hexformat('Kernel'), zone)
                elif 'shadow' in zone:
                    modify(shadow, zone)
                else:
                    modify(color2, zone)
        elif "head" in key:
            color1 = colorengine.hexformat('sensors')
            color2 = colorengine.modifycolor(color1,25)
            color3 = colorengine.shadowcolor(color2)
            reflection = colorengine.reflectioncolor(color2)
            for zone in head:
                if 'reflection' in zone:
                    modify(reflection, zone)
                elif 'eyebrows' in zone:
                    modify(color1, zone)
                elif 'eyes' in zone:
                    modify(color3, zone)
                else:
                    modify(color2, zone)
        elif "body" in key:
            color1 = colorengine.hexformat('CPU')
            color2 = colorengine.modifycolor(color1,20)
            color3 = colorengine.modifycolor(color1,-10)
            shadow = colorengine.shadowcolor(color1)
            reflection = colorengine.reflectioncolor(color1)
            for zone in body:
                if 'reflection' in zone:
                    modify(reflection, zone)
                if 'leg' in zone:
                    modify(color2, zone)
                elif 'skin' in zone:
                    modify(color3, zone)
                else:
                    modify(color1, zone)
        elif "torso" in key:
            color1 = colorengine.hexformat('Net')
            color2 = colorengine.modifycolor(color1,40)
            shadow = colorengine.shadowcolor(color1)
            for zone in torso:
                if 'shadow' in zone:
                    modify(shadow, zone)
                elif 'belly' in zone:
                    modify(color2, zone)
                else:
                    modify(color1, zone)
        elif "left_palm" in key:
            color1 = colorengine.hexformat('USB')
            color2 = colorengine.modifycolor(color1,-50)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color1)
            for zone in left_palm:
                if 'reflection' in zone:
                    modify(reflection, zone)
                elif 'shadow_1' in zone:
                    modify(shadow, zone)
                elif 'shadow_2' in zone:
                    modify(color2, zone)
                else:
                    modify(color1, zone)
        elif "right_palm" in key:
            color1 = colorengine.hexformat('support')
            color2 = colorengine.modifycolor(color1,20)
            reflection = colorengine.reflectioncolor(color1)
            shadow = colorengine.shadowcolor(color1)
            for zone in right_palm:
                if 'reflection' in zone:
                    modify(reflection, zone)
                elif 'shadow_1' in zone:
                    modify(shadow, zone)
                elif 'shadow' in zone:
                    modify(reflection, zone)
                else:
                    modify(color1, zone)

# Add argument item to tux_mod.svg
def addaccessory(item):
    """
        takes the name of an item and add it to the specified file
    """

    global pathtomod
    global path

    DOMTree = parse(pathtomod)
    f=open(pathtomod, "w")
    svg = DOMTree.documentElement
    newElement = DOMTree.createElement("g")
    newElement.setAttribute("id","mark")
    svg.appendChild(newElement);
    f.write(DOMTree.toprettyxml())
    f.close()

    f=open(pathtomod, "r")
    regex="<g id=\"mark\"/>"
    regex=re.escape(regex)
    matches=re.split(regex, f.read(), 1)
    tuxSvg1=matches[0]
    tuxSvg2=matches[1]
    f.close()

    pathtoitem = os.path.join(path, "sprays/")
    f=open(pathtoitem+item+".svg", "r")
    regex="id=\""+item+"\""
    regex=re.escape(regex)
    tuxSvg1=tuxSvg1+"<g\n\t\t\t"+regex
    matches=re.split(regex, f.read(), 1)
    match=matches[1]
    regex="<g id=\"mark\"/>"
    regex=re.escape(regex)
    matches=re.split(regex, match, 1)
    f.close()

    f=open(pathtomod, "w")
    f.write(tuxSvg1+matches[0]+tuxSvg2)
    f.close()

# Apply color in hexadecimal to bodypart
def modify(hexacolor, bodypart):
    """
        modify the bodypart with the color given
    """
    global pathtomod

    DOMTree = xml.dom.minidom.parse(pathtomod)
    f=open(pathtomod, "w")
    svg = DOMTree.documentElement
    paths = svg.getElementsByTagName("path")
    for path in paths:
        if path.getAttribute("id")==bodypart:
            if path.hasAttribute("style"):
                style = path.getAttribute("style")
                regex="fill:"
                matches=re.split(regex, style, 1)
                newStyle=matches[0]+"fill:"
                regex=";"
                style=matches[1]
                matches=re.split(regex, style, 1)
                newStyle=newStyle+"#"+hexacolor+";"+matches[1]
                path.setAttribute("style", newStyle)
            else:
                print(bodypart+" : <style> not found")
    f.write(DOMTree.toprettyxml())
    f.close()

# Initialize tux_mod.svg
def tuxinit():
    """
        go back to the original Tux
    """
    global path
    global pathtomod
    pathtotux = os.path.join(path, "sprays/original_tux.svg")
    tux = open(pathtotux).read()
    f=open(pathtomod, "w+")
    f.write(tux)
    f.close()
