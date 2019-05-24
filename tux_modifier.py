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

#def modifCouleurPupilleGauche(couleur):
    #regex= "pupille_gauche"
    #matches = re.split(regex, newSvgFile)
    #test_str = matches[1]
    #print(test_str)
    #regex= "fill:"
    #matches = re.split(regex, test_str, 1)
    #test_str = matches[1]
    #print(test_str)
    #regex= ";"
    #matches = re.split(regex, test_str, 1)
    #fillToReplace = matches[0]
    #print(fillToReplace)
    #fillToReplace = re.escape(fillToReplace)
    #newFill="#ff0000"
    #newSvgFile = re.sub(fillToReplace, newFill, newSvgFile)

def modifCouleurOeilGaucheBlanc(couleur):
    """
        prend en parametre une couleur pour modifier celle du blanc de l'oeil gauche
    """
    svgFile = open("tux_mod.svg").read()
    regex = "oeil_gauche_blanc"
    matches = re.split(regex, svgFile)
    test_str = matches[1]
    regex= "fill:"
    matches = re.split(regex, test_str, 1)
    test_str = matches[1]
    regex= ";"
    matches = re.split(regex, test_str, 1)
    fillToReplace = matches[0]
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

def reinitColor():
    """
        rend a Tux ses couleurs d'origine
    """
    tux = open("original_tux.svg").read()
    f=open("tux_mod.svg", "w")
    f.write(tux)
    f.close()

reinitColor()
print("En quelle couleur voulez vous la paupiere gauche ?")
couleur=input()
modifCouleurPaupiereGauche(couleur)
print("En quelle couleur voulez vous le blanc de l'oeil gauche ?")
couleur=input()
modifCouleurOeilGaucheBlanc(couleur)

#TODO : régler le probleme de la modification de la couleur pour les elements comme la pupille
#TODO : demander la saisie de la couleur par l'utilisateur, voir même du code hexa de la couleur, mais il faut pouvoir vérifier le format de ce code en hexa
#TODO : tout traduire en anglais
#TODO : reinitialiser la couleur de juste la paupiere par exemple
#TODO : generaliser à toutes les parties du corps
