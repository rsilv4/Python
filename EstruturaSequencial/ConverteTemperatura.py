#!/usr/bin/python

grausF = input ("Informe a quantidade de graus em Farenheit: ")
grausCelsius = (5*(grausF-32)/9)

grausC = input ("Informe a quantidade de graus em Celsius: ")
p1 = ((grausC / 5)*9)+32

print "%s graus Farenheit e igual a %s em graus Celsius" %(grausF,grausCelsius)
print "%s graus Celsius e igual a %s em graus Farenheit" %(grausC,p1)





#(grausC / 5) = (grausFarenheit - 32) / 9