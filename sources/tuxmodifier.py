from xml.dom.minidom import parse
import xml.dom.minidom
import re
import xml.sax
import xml.dom

def addaccessory(item, filename,x,y):
    DOMTree = parse(filename)
    f=open(filename, "w")
    svg = DOMTree.documentElement
    newElement = DOMTree.createElement("image")
    newElement.setAttribute("xlink:href",item)
    newElement.setAttribute("x",str(x))
    newElement.setAttribute("y",str(y))
    newElement.setAttribute("height","120")
    newElement.setAttribute("width","140")
    svg.appendChild(newElement);

    f.write(DOMTree.toprettyxml())
    f.close()

def resize(tuxmod, ratio):
    """
        takes a ratio in parameters, between 0.5 and 1.5 included, a filename, and resizes the tux accordingly
    """
    if ratio>=0.5:
        if ratio<=1.5:
            DOMTree = xml.dom.minidom.parse(tuxmod+".svg")
            f=open(tuxmod+".svg", "w")
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
