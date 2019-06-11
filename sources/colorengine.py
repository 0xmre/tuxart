import struct
import configparser

def hexformat(configmenu):
    red = configparser.countconfig('y',configmenu)%255
    green = configparser.countconfig('m',configmenu)%255
    blue = configparser.countconfig('n',configmenu)%255
    res = '%02x%02x%02x' % (red,green,blue)
    return res

def modifycolor(rgbstr,int):
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]

    if red > green and red > blue:
        if green <= 150:
            green = (green + int)%255
        else:
            green=green%150

        if blue <= 150:
            blue = (blue + int)%255
        else:
            blue=blue%150
        # green = (green + int)%255
        # blue = (blue + int)%255
    elif green > blue:
        if blue <= 150:
            blue = (blue + int)%255
        else:
            blue=blue%150

        if red <= 150:
            red = (red + int)%255
        else:
            red=red%150

    else:
        blue=(blue+100)%255
        if green <= 150:
            green = (green + int)%255
        else:
            green=green%150

        if red <= 150:
            red = (red + int)%255
        else:
            red=red%150
        # red = (red+int)%255
        # green = (green+int)%255

    res = '%02x%02x%02x' % (abs(red),abs(green),abs(blue))
    return res

def reflectioncolor(rgbstr):
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]
    if red>green and red>blue:
        green= green + (red-green)*2/3
        blue= blue + (red-blue)*2/3
    elif green>blue:
        blue=blue + (green-blue)*2/3
        red= red + (green-red)*2/3
    else:
        red= red + (blue-red)*2/3
        green= green + (blue-green)*2/3
    res = '%02x%02x%02x' % (int(red),int(green),int(blue))
    return res

def shadowcolor(rgbstr):
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]
    if red>green and red>blue:
        green= green - (red-green)*3/4
        blue= blue - (red-blue)*3/4
    elif green>blue:
        blue= blue - (green-blue)*3/4
        red= red - (green-red)*3/4
    else:
        red= red - (blue-red)*3/4
        green= green - (blue-green)*3/4
    res = '%02x%02x%02x' % (int(red),int(green),int(blue))
    return res
