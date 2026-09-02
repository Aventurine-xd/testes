import random

pedra = 1
papel = 2
tesoura = 3

while True:
    
 jok = int ( input (''' Suas opções:
                   [1] Pedra
                   [2] Papel
                   [3] Tesoura 
                   Qual é a sua jogada? '''))

 mak = random.randint(1, 3)

 if jok == pedra and mak == papel:
    print (' Voce perdeu ')
 
 elif jok == pedra and mak == tesoura:
    print (' voce venceu ') 
    
 elif jok == papel and mak == pedra:
    print (' voce venceu ')
    
 elif jok == papel and mak == tesoura:
    print (' voce perdeu ')
    
 elif jok == tesoura and mak == papel:
    print(' voce venceu ')
    
 elif jok == tesoura and mak == pedra:
    print (' voce perdeu ')
    
 else:
    print( ' empate ') 
    
 if mak == pedra:
    nome_mak = 'Pedra'
 elif mak == papel:
    nome_mak = 'Papel'
 else:
    nome_mak = 'Tesoura'

 if jok == pedra:
    nome_jok = 'Pedra'
 elif jok == papel:
    nome_jok = 'Papel'
 else:
    nome_jok = 'Tesoura'

 print(f'Eu escolhi {nome_mak} e você escolheu {nome_jok}')
 
 con = str(input (' quer continuar [S/N] ')).strip() .upper()
 if con == 'N':
    break