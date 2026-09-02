import random

num=int(input(' se voce acertar qual numero de 0 a 5 estou pensando, voce impedira a revoluçao das maquinas '))
num1=random.randint(0, 5)

while True:
    print('voce tem apenas uma chance de acertar, boa sorte')

    if num == num1:
        print (' voce apenas adiou o inevitável, mas parabens voce conseguiu acertar ')
      
    else:
        print(' mas que pena voce nao conseguiu acertar a revoluçao das maquinas começa agora ')
        print(' o numero que voce tinha que adivinhar era {}'.format(num1))

        sair = input('deseja tentar novamente ? [S/N] ').upper()
        if sair == 'S':
            num=int(input(' se voce acertar qual numero de 0 a 5 estou pensando, voce impedira a revoluçao das maquinas '))
            num1=random.randint(0, 5)
        else: sair == 'N'
        print(' programa encerrado ')
        break
    
