
================================= WELCOME TO TUXART ===============================
v4


![tux gif](tuxartlogo.gif)


This program will fetch for your running Kernel's configuration file and then generate an unique Tux based on the current active configurations on your kernel.

The script will fetch in the default folders /boot and /proc for a configuration file.

An arbitrary kernel configuration file can be passed as argument, output file will be stored in CustomTux folder


DOWNLOAD AND INSTALL INSTRUCTIONS:

- Open a terminal and type "git clone https://github.com/HommeOursPorc/tuxart"

- Then from tuxart/ folder type "pip3 install ." (sudo may be needed in orther to run install)

(pip3 and python3 are needed in order to install and run the program, type sudo apt-get install python3 and sudo apt-get -y install python3-pip)


                                    EXECUTE ME!!

                    - from tuxart/sources type "./tuxart.sh [.config file]"





HOW TO GENERATE A GRID OF RANDOM TUX:

Run this script if you already have a linux kernel.*
You can also define the number of random Tux in your grid as argument or the script will create by default 5 different Tux and assemble them in a grid.
You will find your TuxFamily.png in the folder TuxGallery/

                                    EXECUTE ME!!

                   - from tuxart/install type "./demo-png.sh [path to kernel folder] [number of tux]"


*If you don't have a kernel, download one from https://www.linux-mips.org/pub/linux/mips/kernel/v4.x/
Unpack the archive and run ./demo-png.sh with the path to the archive's folder passed as argument.
