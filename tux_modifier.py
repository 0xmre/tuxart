import re

#left eye :
#paupiere_gauche
#oeil_gauche_reflet_interieur_pupille
#pupille_gauche
#oeil_gauche_blanc


def modifCouleurPaupiereGauche(couleur):
    """
        prend en parametre une couleur pour modifier celle de la paupiere gauche
    """
    svgFile = open("tux_mod.svg").read()
    #svgFile = "id=\"paupiere_gauche\"style=\"fill:url(#radialGradient18832);fill-opacity:1;stroke:none\""
    regex = "paupiere_gauche"
    matches = re.split(regex, svgFile)
    test_str = matches[1]
    #print(test_str)
    regex= "fill:"
    matches = re.split(regex, test_str, 1)
    test_str = matches[1]
    #print(test_str)
    regex= ";"
    matches = re.split(regex, test_str, 1)
    fillToReplace = matches[0]
    #print(fillToReplace)
    fillToReplace = re.escape(fillToReplace)
    if couleur == "rouge" :
        newFill="#ff0000"
    elif couleur == "bleu":
        newFill="#0000ff"
    newSvgFile = re.sub(fillToReplace, newFill, svgFile)
    newSvgFile.format()
    f=open("tux_mod.svg", "w")
    f.write(newSvgFile)
    f.close()

def modifCouleurPupilleGauche(couleur):
    svgFile = open("tux_mod.svg").read()
    regex= "pupille_gauche"
    matches = re.split(regex, svgFile)
    newSvgFile = matches[0] + regex
    test_str = matches[1]
    regex= "fill:"
    matches = re.split(regex, test_str, 1)
    test_str = matches[1]
    newSvgFile = newSvgFile + matches[0] + regex
    if couleur == "rouge" :
        newSvgFile=newSvgFile+"#ff0000"
    elif couleur == "bleu":
        newSvgFile=newSvgFile+"#0000ff"
    regex= ";"
    matches = re.split(regex, test_str, 1)
    newSvgFile=newSvgFile+";"+matches[1]
    newSvgFile.format()
    f=open("tux_mod.svg", "w")
    f.write(newSvgFile)
    f.close()

def modifCouleurOeilGaucheBlanc(couleur):
    """
        prend en parametre une couleur en hexa pour modifier celle du blanc de l'oeil gauche
    """
    isHexa = re.search("([A-Fa-f0-9]{6})", couleur)
    if (isHexa):
        svgFile = open("tux_mod.svg").read()
        regex = "oeil_gauche_blanc"
        matches = re.split(regex, svgFile)
        newSvgFile = matches[0] + regex
        test_str = matches[1]
        regex= "fill:"
        matches = re.split(regex, test_str, 1)
        test_str = matches[1]
        newSvgFile = newSvgFile + matches[0] + regex + "#" + couleur
        regex= ";"
        matches = re.split(regex, test_str, 1)
        newSvgFile=newSvgFile+";"+matches[1]
        newSvgFile.format()
        f=open("tux_mod.svg", "w")
        f.write(newSvgFile)
        f.close()
    else:
        print("Mauvaise saisie")

def reinitColor():
    """
        rend a Tux ses couleurs d'origine
    """
    tux = open("original_tux.svg").read()
    f=open("tux_mod.svg", "w")
    f.write(tux)
    f.close()

# reinitColor()
# print("En quelle couleur voulez vous la paupiere gauche ? (bleu ou rouge)")
# couleur=input()
# modifCouleurPaupiereGauche(couleur)
# print("En quelle couleur hexadecimale voulez vous le blanc de l'oeil gauche ? (00ff00 par exemple)")
# couleur=input()
# modifCouleurOeilGaucheBlanc(couleur)
# print("En quelle couleur voulez vous la pupille de l'oeil gauche ? (bleu ou rouge)")
# couleur=input()
# modifCouleurPupilleGauche(couleur)
# print("Done."
