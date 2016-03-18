import os
import sys

arg = str(sys.argv[1:])
arg  = arg.replace("]","")
arg  = arg.replace("[","")
arg  = arg.replace("'","")
 	
str = "espeak -ven-us+f1 --stdout "
str = str + "'"+ arg + "'"
str= str + "-a 300 -s 130 | aplay"

os.system(str)
