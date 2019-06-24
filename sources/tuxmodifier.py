from xml.dom.minidom import parse
import xml.dom.minidom
import re
import xml.sax
import xml.dom
import configparser
import colorengine

#
# Declaration of the different body part of the tux
#
bodypart = ['head','beak','left_eye','right_eye','body','torso','left_palm','right_palm']
# These array are fill with the different part of the tux to modify
head = ['skin_between_eyes', 'head_skin', 'forehead_reflection', 'right_eyebrows', 'left_eyebrows', ]
beak = ['smile', 'beak_shadow_on_eyes', 'beak_bottom_part', 'beak_bottom_part_reflection', 'beak_upper_part', 'beak_upper_part_reflection', 'right_nostril', 'left_nostril', 'beak_right_end']
left_eye = ['white_left_eye', 'left_pupil', 'left_pupil_reflection', 'left_eyelid']
right_eye = ['white_right_eye', 'right_pupil', 'right_pupil_reflection_1', 'right_pupil_reflection_2', 'right_eyelid']
body = ['skin', 'right_leg', 'left_leg', 'right_arm', 'right_arm_reflection', 'neck_reflection', 'skin_reflection', 'right_hand', 'right_hand_reflection_1', 'right_hand_reflection_2', 'left_arm', 'left_arm_reflection']
torso = ['belly', 'torso_shadow', 'shadow_under_beak', 'chest_left_shadow', 'chest_right_shadow', 'chest_middle_shadow', 'belly_shadow']
left_palm = ['left_palm', 'left_palm_shadow_1', 'left_palm_shadow_2', 'left_palm_reflection']
right_palm = ['right_palm_shadow_1', 'right_palm_shadow_2', 'right_palm_shadow_3', 'right_palm', 'right_palm_reflection', 'right_arm_shadow_1', 'right_arm_shadow_2']

def accessoryhandler():
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

def addaccessory(item):
    """
        takes the name of an item and add it to the specified file
    """
    DOMTree = parse("tux_mod.svg")
    f=open("tux_mod.svg", "w")
    svg = DOMTree.documentElement
    newElement = DOMTree.createElement("g")
    newElement.setAttribute("id","mark")
    svg.appendChild(newElement);
    f.write(DOMTree.toprettyxml())
    f.close()

    f=open("tux_mod.svg", "r")
    regex="<g id=\"mark\"/>"
    regex=re.escape(regex)
    matches=re.split(regex, f.read(), 1)
    tuxSvg1=matches[0]
    tuxSvg2=matches[1]
    f.close()

    f=open("sprays/"+item+".svg", "r")
    regex="id=\""+item+"\""
    regex=re.escape(regex)
    tuxSvg1=tuxSvg1+"<g\n\t\t\t"+regex
    matches=re.split(regex, f.read(), 1)
    match=matches[1]
    regex="<g id=\"mark\"/>"
    regex=re.escape(regex)
    matches=re.split(regex, match, 1)
    f.close()

    f=open("tux_mod.svg", "w")
    f.write(tuxSvg1+matches[0]+tuxSvg2)
    f.close()

def resize(ratio):
    """
        takes a ratio in parameters, between 0.5 and 1.5 included, a filename, and resizes the tux accordingly
    """
    if ratio>=0.5:
        if ratio<=1.5:
            DOMTree = xml.dom.minidom.parse(tuxmod+".svg")
            f=open("tux_mod.svg", "w")
            svg = DOMTree.documentElement
            gs = svg.getElementsByTagName("g")
            for g in gs:
                if g.getAttribute("id")=="layer1":
                    if g.hasAttribute("transform"):
                        transform = g.getAttribute("transform")
                        regex="scale("
                        regex=re.escape(regex)
                        matches=re.split(regex, transform, 1)
                        newTransform=matches[0]+"scale("
                        regex=" 1)"
                        regex=re.escape(regex)
                        transform=matches[1]
                        matches=re.split(regex, transform, 1)
                        newTransform=newTransform+str(ratio)+" 1)"+matches[1]
                        newTransform.format()
                        g.setAttribute("transform", newTransform)
            f.write(DOMTree.toprettyxml())
            f.close()


def modify(hexacolor, bodypart):
    """
        modify the bodypart with the color given
    """
    DOMTree = xml.dom.minidom.parse("tux_mod.svg")
    f=open("tux_mod.svg", "w")
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

def reinit():
    """
        go back to the original Tux
    """
    tux = open("sprays/original_tux.svg").read()
    f=open("tux_mod.svg", "w")
    f.write(tux)
    f.close()

def modify_skin(hexacolor):
    modify(hexacolor, "skin")

def modify_right_leg(hexacolor):
    modify(hexacolor, "right_leg")

def modify_left_leg(hexacolor):
    modify(hexacolor, "left_leg")

def modify_head_skin(hexacolor):
    modify(hexacolor, "head_skin")

def modify_belly(hexacolor):
    modify(hexacolor, "belly")

def modify_torso_shadow(hexacolor):
    """
        modify the shadow on the torso, under the beak
    """
    modify(hexacolor, "torso_shadow")

def modify_shadow_under_beak(hexacolor):
    """
        modify the thin shadow right under the beak
    """
    modify(hexacolor, "shadow_under_beak")

def modify_white_left_eye(hexacolor):
    modify(hexacolor, "white_left_eye")

def modify_white_right_eye(hexacolor):
    modify(hexacolor, "white_right_eye")

def modify_beak_shadow_on_eyes(hexacolor):
    modify(hexacolor, "beak_shadow_on_eyes")

def modify_skin_between_eyes(hexacolor):
    modify(hexacolor, "skin_between_eyes")

def modify_forehead_reflection(hexacolor):
    modify(hexacolor, "forehead_reflection")

def modify_right_pupil(hexacolor):
    modify(hexacolor, "right_pupil")

def modify_right_pupil_reflection_1(hexacolor):
    modify(hexacolor, "right_pupil_reflection_1")

def modify_right_pupil_reflection_2(hexacolor):
    modify(hexacolor, "right_pupil_reflection_2")

def modify_right_eyelid(hexacolor):
    modify(hexacolor, "right_eyelid")

def modify_right_eyebrows(hexacolor):
    modify(hexacolor, "right_eyebrows")

def modify_left_eyebrows(hexacolor):
    modify(hexacolor, "left_eyebrows")

def modify_left_pupil(hexacolor):
    modify(hexacolor, "left_pupil")

def modify_left_pupil_reflection(hexacolor):
    modify(hexacolor, "left_pupil_reflection")

def modify_beak_bottom_part(hexacolor):
    modify(hexacolor, "beak_bottom_part")

def modify_beak_bottom_part_reflection(hexacolor):
    modify(hexacolor, "beak_bottom_part_reflection")

def modify_smile(hexacolor):
    modify(hexacolor, "smile")

def modify_beak_upper_part(hexacolor):
    modify(hexacolor, "beak_upper_part")

def modify_beak_upper_part_reflection(hexacolor):
    modify(hexacolor, "beak_upper_part_reflection")

def modify_right_nostril(hexacolor):
    modify(hexacolor, "right_nostril")

def modify_left_nostril(hexacolor):
    modify(hexacolor, "left_nostril")

def modify_beak_right_end(hexacolor):
    modify(hexacolor, "beak_right_end")

def modify_left_eyelid(hexacolor):
    modify(hexacolor, "left_eyelid")

def modify_right_arm(hexacolor):
    modify(hexacolor, "right_arm")

def modify_right_arm_reflection(hexacolor):
    modify(hexacolor, "right_arm_reflection")

def modify_chest_left_shadow(hexacolor):
    modify(hexacolor, "chest_left_shadow")

def modify_chest_right_shadow(hexacolor):
    modify(hexacolor, "chest_right_shadow")

def modify_chest_middle_shadow(hexacolor):
    modify(hexacolor, "chest_middle_shadow")

def modify_belly_shadow(hexacolor):
    modify(hexacolor, "belly_shadow")

def modify_neck_reflection(hexacolor):
    modify(hexacolor, "neck_reflection")

def modify_right_palm_shadow_1(hexacolor):
    """
        modify the shadow made by the right the palm on the body
    """
    modify(hexacolor, "right_palm_shadow_1")

def modify_right_palm_shadow_2(hexacolor):
    """
        modify the interior part of the shadow on the right palm
    """
    modify(hexacolor, "right_palm_shadow_2")

def modify_right_palm_shadow_3(hexacolor):
    """
        modify the exterior part of the shadow on the right palm
    """
    modify(hexacolor, "right_palm_shadow_3")

def modify_right_palm(hexacolor):
    modify(hexacolor, "right_palm")

def modify_right_palm_reflection(hexacolor):
    modify(hexacolor, "right_palm_reflection")

def modify_skin_reflection(hexacolor):
    modify(hexacolor, "skin_reflection")

def modify_unknown_part(hexacolor):
    """
        this part isn't visible on the original Tux. It mays be under other elements.
    """
    modify(hexacolor, "unknown_part")

def modify_right_arm_shadow_1(hexacolor):
    """
        Shadow made by the right hand on the right palm. Largest and brightest part.
    """
    modify(hexacolor, "right_arm_shadow_1")

def modify_right_arm_shadow_2(hexacolor):
    """
        Shadow made by the right hand on the right palm. Smallest and darkest part.
    """
    modify(hexacolor, "right_arm_shadow_2")

def modify_right_hand(hexacolor):
    modify(hexacolor, "right_hand")

def modify_right_hand_reflection_1(hexacolor):
    modify(hexacolor, "right_hand_reflection_1")

def modify_right_hand_reflection_2(hexacolor):
    modify(hexacolor, "right_hand_reflection_2")

def modify_left_arm(hexacolor):
    modify(hexacolor, "left_arm")

def modify_left_arm_reflection(hexacolor):
    modify(hexacolor, "left_arm_reflection")

def modify_left_palm_shadow_1(hexacolor):
    """
        exterior part
    """
    modify(hexacolor, "left_palm_shadow_1")

def modify_left_palm_shadow_2(hexacolor):
    """
        interior part
    """
    modify(hexacolor, "left_palm_shadow_2")

def modify_left_palm(hexacolor):
    modify(hexacolor, "left_palm")

def modify_left_palm_reflection(hexacolor):
    modify(hexacolor, "left_palm_reflection")
