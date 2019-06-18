import struct
import configparser

# Construction of the triplet RGB
def hexformat(configmenu):
    red = configparser.countconfig('y',configmenu)%255
    green = configparser.countconfig('m',configmenu)%255
    blue = configparser.countconfig('n',configmenu)%255
    res = '%02x%02x%02x' % (red,green,blue)
    return res

# Add some modification on the hexa color
def modifycolor(rgbstr,int):
    # Reconstructrion of RGB triplet
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
        blue=(blue-100)%255
        if green <= 150:
            green = (green + int)%255
        else:
            green=green%150

        if red <= 150:
            red = (red + int)%255
        else:
            red=red%150

    res = '%02x%02x%02x' % (abs(red),abs(green),abs(blue))
    return res

# Reduce shadow of the hexa color
def reflectioncolor(rgbstr):
    # Reconstructrion of RGB triplet
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

# Increase shadow of the hexa color
def shadowcolor(rgbstr):
    # Reconstructrion of RGB triplet
    rgbtriplet = struct.unpack('BBB',bytes.fromhex(rgbstr))
    red = rgbtriplet[0]
    green = rgbtriplet[1]
    blue = rgbtriplet[2]

    if red>green and red>blue:
        green= green - (red-green)*1/2
        blue= blue - (red-blue)*1/2
    elif green>blue:
        blue= blue - (green-blue)*1/2
        red= red - (green-red)*1/2
    else:
        red= red - (blue-red)*1/2
        green= green - (blue-green)*1/2
    res = '%02x%02x%02x' % (int(red),int(green),int(blue))
    return res
