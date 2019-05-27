
# Pour run le script:
#   depuis le dossier linux-4.13.3 executer la commande
#   make scriptconfig SCRIPT=demo/demo_1.py

import sys
# necessity to add the path for calling module in different folder
sys.path.insert(0,'/TuxArt/linux-4.13.3/Kconfiglib/') # kconfiglib's path
import kconfiglib
sys.path.insert(0,'~/TuxArt/includes/') # config_parser & tux_modifier's path
from config_parser import is_CONFIG_FOO_enable
from tux_modifier import *


def main():
    # parse .config file
    kconf = kconfiglib.Kconfig(sys.argv[1])

    # check if the value of SGI_IP22 is y
    # (essayer SGI_IP27 pour rendre faux la fonction)
    if is_CONFIG_FOO_enable(kconf.top_node,"SGI_IP22"):
        modifCouleurPupilleGauche("rouge")

        #modifCouleurOeilGaucheBlanc("bleu")
        #print "mauvaise saisie", NANI

        modifCouleurPaupiereGauche("0x000000")
        #/!\ probleme avec la variable newfill

    else:
        reinitColor()

if __name__=="__main__":
    main()
