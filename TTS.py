import os
import sys

arg = str(sys.argv[1:])
arg  = arg.replace("]","")
arg  = arg.replace("[","")
arg  = arg.replace("'","")
 	
str = "espeak -ven-us_uk-north+f1 --stdout "
str = str + "'"+ arg + "'" 
str= str + "-a 1020 -s 150 | aplay"
print arg
os.system(str)
