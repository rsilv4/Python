#!/usr/bin/python

print "++++ Rendimento Diario ++++"

PESOESTAB=50
VMULTA=4.00

peso = float (input("Informe o peso dos peixeis: "))
if peso > PESOESTAB:
    excesso = (peso - PESOESTAB)
    
    multa = excesso * VMULTA
    print "O peso informado foi de %s, foi execedido %s quilos e o valor da multa sera de %s" %(peso,excesso,multa)
else:
    print "O peso informado e de %s, nao existe multa a se pagar" %peso