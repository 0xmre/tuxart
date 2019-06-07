
================================= WELCOME TO TUXART ===============================
v3


This program will fetch for your running Kernel's configuration file and then generate an unique Tux based on the current active configurations on your kernel.

The script will fetch in the default folders /boot and /proc for a configuration file.

An arbitrary kernel configuration file can be passed as argument, output file will be stored in CustomTux folder


DOWNLAOD AND INSTALL INSTRUCTIONS:

- Open a terminal then type "git clone https://github.com/HommeOursPorc/TuxArt.git"
- from tuxart/ folder type "sudo pip3 install ."

(pip3 and python3 are needed in order to install and run the program, type sudo apt-get install python3 and sudo apt-get -y install python3-pip)


                                    EXECUTE ME!!

                    - from tuxart/install type "./tuxart.sh [.config file]"





EXTRA!
A special demo is available with tuxartdemogif.sh, you will need a linux-4.13.3 kernel version with Kconfglib in it (it is needed in order to generate multiple random configurations).
This script will create 5 different Tux and will assemble them in a .gif, you can find your SuperTux.gif in folder PersonalTux
