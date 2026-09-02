valor = float( input (' qual o valor da compra? '))

pag = int (input (''' qual a forma de pagamento?
                  [1] a vista, Dinheiro / cheque: 10% de desc.
                  [2] a vista cartão: 5% de desc.
                  [3] em 2x no cartão: preço normal.
                  [4] 3x ou mais no cartão: 20% de juros 
                  '''))

if pag == 1 :
    print(f' sua compra ficou no valor de {valor-(valor*10/100)} com 10% de desc ')
    
elif pag == 2 :
    print(f' sua compra ficou em {valor-(valor*5/100)} com 5% de desc no cartão ')
    
elif pag == 3 :
    print (f' sua compra ficou em {valor} em 2x de {valor/2} ')
    
elif pag == 4 :
        ves = int (input('em quantas veses quer parcelar ? ')) 
        
        tot = valor + (valor*20/100)
        parcela = tot / ves
        
        print (f' sua compra ficou em {tot:.2f} com {ves} parcelas de {parcela:.2f} ')

else :
    print ('forma de pagamento invaçida ')
        