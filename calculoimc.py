
print("bem-vindo a calculadora de Indice de Massa Corporal")
nome=str(input('digite seu nome'))
idade=int(input('digite sua idade'))
print('vamos para o calculo')
peso=float(input('digite seu peso em KG'))
altura=float(input('digite sua altura em metros'))
imc=(peso/(altura*altura))
print(imc)
if imc <16:
    print('Muito abaixo do peso');
elif imc <17 :
    print("abaixo do peso1");
elif imc >18 :
    print("peso normal")
elif imc >25 :
    print("acima do peso")
elif imc >30 :
    print("obesidade 1" )
elif imc >35 :
    print("obesidade 2")
else:
    print("obeidade 3")    
    
    
    
