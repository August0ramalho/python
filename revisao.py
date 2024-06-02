#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
hrs_trabalhadas=float(input('digite quantas horas você trablhou este mês:'))
qtd_horas_trabalhadas=float(input('digite quanto que vale suas horas trabalhadas:'))
salario=(hrs_trabalhadas*qtd_horas_trabalhadas)
print('este é o seu salário líquido:',salario)
IR=salario*0.11
print('valor do imposto de renda',IR)
INSS=(salario*0.08)
print('valor do INSS',INSS)
SINDICATO=(salario*0.05)
print('valor descontado do Sindicato ',SINDICATO)
salario_bruto=(salario-IR-INSS-SINDICATO)
print('est é seu salário bruto',salario_bruto)