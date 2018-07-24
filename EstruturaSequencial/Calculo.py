#!/usr/bin/python

num1 = input ("Informe um numero inteiro: ")
num2 = input ("Informe outro numero inteiro: ")
num3 = float(raw_input ("Informe um numero decimal: "))

a = (num1*2) + (num2/2)
b = (num1*3) + num3
c = num3**3

print "a - o produto do dobro do primeiro com metade do segundo e: %s" %a
print "b - a soma do triplo do primeiro com o terceiro e: %s" %b
print "c - o terceiro elevado ao cubo e: %s" %c