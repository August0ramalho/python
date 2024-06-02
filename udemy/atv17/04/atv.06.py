#6)	Faça um programa que exiba na tela todos os números primos entre 1 e 100. Um número primo é
# aquele que é divisível somente por ele mesmo e por 1.

for vetor in range(1,100):
    if vetor%2 !=0 and vetor%3 !=0 and vetor%5 !=0 and vetor%7 !=0:
        print(vetor)
    elif vetor == 2 or vetor==3 or vetor==5  or vetor==7:
        print(vetor)