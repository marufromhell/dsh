Python cli script runner for the flipper zero with python and js***** support.   
You must have a active serial connection usually /dev/ttyACM0  
If your flipper is on a different tty, use -d # to specify ACM number  
  
# Command syntax  
- -d Device number(default 0)  
- dsh script  
#  dsh scripting  
Flipper cli commands are put normally  
Python is wrapped in curly brackets  
To inline comment just use {#comment}  
if you want a full line comment use:  
`#comment`  
Javascript can be uploaded with "upload LOCAL_NAME REMOTE_PATH" and run it with cli commands. but it sucks so maybe dont use it  
If you want to use micropython(COMPLETELY UNSUPPORTED BTW), you can also use upload, because its no longer language specific

I found a really hacky way to support dsh scripting in vscode, just click on "plain text" at bottom right while editing a script, and configure file association for ".dsh" as Lua. There pretty similar and wont throw hundreds of errors like python.  

# install  
git clone https://github.com/marufromhell/dsh.git && cd dsh && mv dsh ~/.local/bin/dsh

# Read the wiki bruz


# GOALS  
* Onboard python using mp-flipper or similar.
* Better file handling functions.
