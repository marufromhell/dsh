Script runner for the flipper zero.  
You must have a active serial connection usually /dev/ttyACM0  
If your flipper is on a different tty, use -d # to specify ACM number  
  
# Command syntax  
- -d Device number(default 0)  
- dsh script  
#  dsh scripting  
Flipper cli commands are put normally  
Python is wrapped in curly brackets  
Python support is extremely limited so i would recomend using a python module and importing it.  
# install  
git clone https://github.com/marufromhell/dsh.git && cd dsh && mv dsh ~/.local/bin/dsh
