#!/usr/bin/python

print "++++ Calculo de Tinta ++++"

REND=3
TAMLATA=18
VALORLATA=80.00

Metragem = float (input ("Informe o tamanho da area a ser pintada em Metro quadrados: "))
QtdLitrosTinta = Metragem / REND
QtdLatas = round((QtdLitrosTinta / TAMLATA),0)

if QtdLatas < 1.0 :
    print "Sera necessario %s Litros de tinta, voce precisa comprar 1 Lata de 18 Litros" %QtdLitrosTinta
    Total = VALORLATA
    print "Valor a ser pago: R$%s"%Total
else:
    print "Sera necessario %s Litros de tinta, voce precisa comprar %s latas de 18 Litros para essa metragem" %(QtdLitrosTinta,float(QtdLatas))
    Total = QtdLatas * VALORLATA
    print "Valor a ser pago: R$%s"%Total