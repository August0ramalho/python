#4)	Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
#crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento
#de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
#do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

def calcular_anos_populacao(popua,crescimentoa, popub,crescimentob):
    anos = 0
    if popua <= popub:
        popua *= 1 + crescimentoa / 100
        popub *= 1 + crescimentob / 100
        anos += 1
    print( anos)

PA = 80000
CA= 3
PB = 200000
CB = 1.5

anos_necessarios = calcular_anos_populacao(PA,CA,PB, CB)

print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")