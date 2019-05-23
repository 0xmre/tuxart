import re

#left eye :
#paupiere_gauche
#oeil_gauche_reflet_interieur_pupille
#pupille_gauche
#oeil_gauche_blanc



#svgFile = open("original_tux.svg").read()
svgFile = "id=\"paupiere_gauche\"style=\"fill:url(#radialGradient18832);fill-opacity:1;stroke:none\""
regex = "paupiere_gauche"
matches = re.split(regex, svgFile)
test_str = matches[1]
print(test_str)
regex= "fill:"
matches = re.split(regex, test_str, 1)
test_str = matches[1]
print(test_str)
regex= ";"
matches = re.split(regex, test_str, 1)
fillToReplace = matches[0]
print(fillToReplace)
fillToReplace = re.escape(fillToReplace)
newFill="#ff0000"
newSvgFile = re.sub(fillToReplace, newFill, svgFile)
print(newSvgFile)
#f=open("tux_mod.svg")
#f.write(newSvgFile)
#f.close()
