from xml.dom.minidom import parse
import xml.dom.minidom
import re
import xml.sax
import xml.dom

def modify_left_eyelid(hexacolor):
    """
        modify the left eyelid with the color given
    """
    DOMTree = xml.dom.minidom.parse("tux_mod.svg")
    f=open("tux_mod.svg", "w")
    svg = DOMTree.documentElement
    if svg.hasAttribute("id"):
        print("id svg : %s" % svg.getAttribute("id"))
    paths = svg.getElementsByTagName("path")
    for path in paths:
        if path.getAttribute("id")=="paupiere_gauche":
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
    f.write(DOMTree.toprettyxml())
    f.close()

def reinit():
    """
        go back to the original Tux
    """
    tux = open("original_tux.svg").read()
    f=open("tux_mod.svg", "w")
    f.write(tux)
    f.close()
