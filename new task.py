
import sys


def hello(name):
    if name == None or name == "":
        return 'Hello, World!'
    else: 
        return 'Hello,' + name + '!'
    
lista = (sys.argv)

text= ""

for nume in lista[1:]:
    text += " " + nume
    
print(hello(text))