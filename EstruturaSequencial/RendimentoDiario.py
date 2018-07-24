#!/usr/bin/python

print "++++ Rendimento Diario ++++"

PESOESTAB=50
VMULTA=4.00

peso = float (input("Informe o peso dos peixeis: "))
excesso = (peso - PESOESTAB)

multa = excesso * VMULTA

print "Peso informado: %s" %peso
print "Peso excedido: %s" %excesso
print "Valor da multa: %s" %multa