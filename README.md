
================================= WELCOME TO TUXART ===============================



![tux gif](SuperTux.gif)


This program will fetch for your running Kernel's configuration file and then generate an unique Tux based on the current active configurations on your kernel.

The script will fetch in the default folders /boot and /proc for a configuration file.

An arbitrary kernel configuration file can be passed as argument, output file will be stored in CustomTux folder


DOWNLOAD AND INSTALL INSTRUCTIONS:

- Open a terminal and type "git clone https://github.com/HommeOursPorc/tuxart"

- Then from tuxart/ folder type "pip3 install ." (sudo may be needed in orther to run install)

(pip3 and python3 are needed in order to install and run the program, type sudo apt-get install python3 and sudo apt-get -y install python3-pip)


                                    EXECUTE ME!!

                    - from tuxart/sources type "./tuxart.sh"

- If you want to pass your custom configuration file:

                    - from tuxart/sources type "./tuxart.sh -f [configuration file]"


- Type "./tuxart.sh -h" or "./tuxart.sh --help" for help from terminal


OPTIONS:

Various options are available if you already have a linux kernel.*
You can either : generate a grid of Tux
                 generate a .gif of Tux
                 summon elemenTux ( all configurations set to yes, no or module )

                                    EXECUTE ME!!

                   - from tuxart/sources type
                        ./tuxart.sh --grid [path to kernel folder] [number of tux, default = 4]
                        ./tuxart.sh --gif [path to kernel folder] [number of tux, default = 4]
                        ./tuxart.sh --rgb [path to kernel folder]


*If you don't have a kernel, download one from https://www.linux-mips.org/pub/linux/mips/kernel/v4.x/
Unpack the archive and run ./demo-png.sh with the path to the archive's folder passed as argument.
