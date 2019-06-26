

# WELCOME TO TUXART



![tux grid](examples/TuxFamily.png)


This program will fetch for your running Kernel's configuration file and then generate an unique Tux based on the current active configurations on your kernel.

The script will fetch in the default folders /boot and /proc for a configuration file.

An arbitrary kernel configuration file can be passed as argument, output file will be stored in ~/Pictures/CustomTux


## DOWNLOAD AND INSTALL INSTRUCTIONS:

- From terminal type
-`sudo pip3 install tuxart --install-option="--install-scripts=/usr/local/bin"`



### RUN TUXART

- From terminal type
-`tuxart`

If you want to pass your custom configuration file:
- From terminal type
 -`tuxart -f [configuration file]`

Type `tuxart -h` or `tuxart --help` for help from terminal


## OPTIONS:

Various options are available if you already have a linux kernel.*
You can either :
- **generate a grid of Tux**
- **generate a .gif of Tux**
                 ![tux gif][examples/SuperTux.gif]
 - **summon elemenTux** ( all configurations set to yes, no or module )

### RUN OPTIONS

   - From terminal type :
	   -`tuxart --grid [path to kernel folder] [number of tux, default = 4]`
       -`tuxart --gif [path to kernel folder] [number of tux, default = 4]`
       -`tuxart --rgb [path to kernel folder]`


*If you don't have a kernel, download one from https://www.linux-mips.org/pub/linux/mips/kernel/v4.x/
Unpack the archive and run ./demo-png.sh with the path to the archive's folder passed as argument.
