


1. # Até 5 Kg Acima de 5 Kg
2. #File Duplo R$ 30.90 por Kg R$ 36.80 por Kg
3. #Alcatra R$ 32.90 por Kg R$ 35.80 por Kg
4. #Picanha R$ 49.90 por Kg R$ 55.80 por Kg


print('1 file Duplo'
      '2 alcatra'
      '3 picanha')

tipo_carne=int(input('qual e o tipo da carne?'))
print('1 para cartão da loja ' 
       '2 para outro metodo de pagamento ')
cartão=int(input('qual é o metodo de pagamento?'))



if tipo_carne==1:
    nome='file duplo'
    quantidade=float(input('quantos kg? '))
    total=quantidade*30.90
    if quantidade>=5:
            total=quantidade*32.90
else:
     total=quantidade *32.90
    
    
    
    
if tipo_carne==2:
    nome='alcatra'
    quantidade=float(input('quantos kg? '))
    
    if quantidade>=5:
        total=quantidade*32.90
else:
    total=quantidade*35.80
        

    
if tipo_carne==3:
    nome='picanha'
    quantidade=float(input('quantos kg? '))
    total=quantidade*49.90
    if quantidade>=5:
            total=quantidade*32.90
else:
    total=quantidade*35.80
        
if cartão==1:
    conclusão='sim'
    total = total -(total*0.05) 
    round (2.0)
else:
    conclusão='não'
    print('faça o cartão da loja' )
    
    
    
print('********nota fiscal**********')
print('Produto',nome)
print( 'Usa cartao?', cartão)
print('o custo total é de R$', total)