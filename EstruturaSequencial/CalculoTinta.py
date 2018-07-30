#!/usr/bin/python

print "++++ Calculo de Tinta ++++"

REND=6
TAMLATA=18
TAMGALAO=3.6
VALORLATA=80.00
VALORGALAO=25.00

Metragem = float (input ("Informe o tamanho da area a ser pintada em Metro quadrados: "))
QtdLitrosTinta = Metragem / REND
QtdLatas = (QtdLitrosTinta / TAMLATA)
TotalLatas = QtdLatas * VALORLATA
QtdGalao = (QtdLitrosTinta / TAMGALAO)
TotalGalao = QtdGalao * VALORGALAO

SobraLatas = (QtdLitrosTinta % TAMLATA)
RestGalao = round((SobraLatas / TAMGALAO),0) 
print "sobra", SobraLatas
print "resto galao", RestGalao

print "Voce ira utilizar %s litros de tinta: " %QtdLitrosTinta

print "Quantidade de galoes de 3,16 litros: %s - Total a ser pago: %s"%(QtdGalao,TotalGalao)
print "Quantidade de latas de 18 litros: %s - Total a ser pago: %s"%(QtdLatas,TotalLatas)


