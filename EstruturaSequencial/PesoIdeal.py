#!/usr/lib/python

sexo = raw_input("Informe seu genero (M) ou (F): ")

if sexo == "M" or sexo == "m" :
    altura = input("Informe sua altura: ")
    pesoideal = (72.7*altura) - 58
    print "Seu peso idela e: %s" %pesoideal
elif sexo == "F" or sexo == "f":
    altura = input("Informe sua altura: ")
    pesoideal = (62.1*altura) - 44.7
    print "Seu peso idela e: %s" %pesoideal
else:
    print "Dados invalidos"


