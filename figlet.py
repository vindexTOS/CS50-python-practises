from pyfiglet import Figlet 
import sys

figlet = Figlet()

s= input("Input text: " )

if  '-f' in s  or  "-font" in s :
    f = s.split()[1]
    figlet.getFonts()
    figlet.setFont(font=f)
    c = input("Input: ")
    print(figlet.renderText(c))
    sys.exit(1)
else:
    print(figlet.renderText(s))
    sys.exit(0)
# slant