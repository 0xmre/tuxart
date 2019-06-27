import struct
import configparser


# Construction of the RGB triplet
# base on the triplet (y,m,n)
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

    # Modify red,green or blue depending on the bigger value
    if red > green and red > blue:
        if red <150: red = (red+100)

        if (green+int)<201: green = (green+int)%200

        if (blue+int)<231: blue = (blue+int)%230
    elif green > blue:
        if green<201: green = (green+55)

        if (blue+int)<231: blue = (blue+int)%230

        if (red+int)<151: red = (red+int)%150
    else:
        if blue<150: blue = (blue+150)

        if (green+int)<201: green = (green+int)%200

        if (red+int)<201: red = (red+int)%200


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
        green= green + (red-green)*1/2
        blue= blue + (red-blue)*1/2
    elif green>blue:
        blue=blue + (green-blue)*1/2
        red= red + (green-red)*1/2
    else:
        red= red + (blue-red)*1/2
        green= green + (blue-green)*1/2
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
        green= green - (red-green)*1/4
        blue= blue - (red-blue)*1/4
    elif green>blue:
        blue= blue - (green-blue)*1/4
        red= red - (green-red)*1/4
    else:
        red= red - (blue-red)*1/4
        green= green - (blue-green)*1/4
    res = '%02x%02x%02x' % (abs(int(red)),abs(int(green)),abs(int(blue)))
    return res
