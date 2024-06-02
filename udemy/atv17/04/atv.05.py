#5)	Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
# número elevado ao segundo número. Não utilize a função de potência da linguagem.
num1=input('digite um numero')
num2=input('digite um numero')
r=num1
for c in (1,num2):
    expoente=r*num2
    r=expoente
print( num1,'^',num2, '=',r)