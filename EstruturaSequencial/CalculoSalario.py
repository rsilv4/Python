#!/usr/bin/python
print "++++ Calcula Salario ++++"

IR=0.11
INSS=0.08
SIND=0.05

CustoHora = input ("Informe o custo da hora trabalhada: ")
HorasTrab = input ("Informe a quantidade de horas trabalhadas no mes: ")

SalarioBruto = CustoHora * HorasTrab
ValorDescIR = SalarioBruto * IR
ValorDescINSS = SalarioBruto * INSS
ValorDescSind = SalarioBruto * SIND
TotalDesc = (ValorDescIR + ValorDescINSS + ValorDescSind)

SalarioLiquido = SalarioBruto - TotalDesc

print "Salario Bruto : R$ %s" %SalarioBruto
print "IR (11) : R$ %s" %ValorDescIR
print "INSS (8) : R$ %s" %ValorDescINSS
print "Sindicato (5) : R$ %s" %ValorDescSind
print "Salario Liquido : R$ %s" %SalarioLiquido