#3)	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.
vetor= input('digite uma palavra')
lista=[]
consoantes=[]
print(vetor)
for c in vetor:
    lista.append(c)
for c in vetor:
    if c =='a':
        lista.remove(c)
    else:
        consoantes.append(c)

for c in vetor:
    if c =='e':
        lista.remove(c)
    else:
        consoantes.append(c)
for c in vetor:
    if c =='i':
        lista.remove(c)
    else:
        consoantes.append(c)
for c in vetor:
    if c =='0':
        lista.remove(c)
    else:
        consoantes.append(c)
for c in vetor:
    if c =='u':
        lista.remove(c)
    else:
        consoantes.append(c)



print(lista)