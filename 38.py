from datetime import datetime

while True:

 ano = int(input('Em que ano você nasceu? '))
 sexo = str(input('Qual é o seu sexo? [M/F] ').strip().upper())

 idade = datetime.now().year - ano

 while sexo not in ['M', 'F']:
        print('Sexo inválido. Por favor, digite M para masculino ou F para feminino.')
        sexo = str(input('Qual é o seu sexo? [M/F] ').strip().upper())

 if sexo == 'M' or sexo == 'F':
    if sexo == 'F':
          print('''Você não é obrigada a se alistar, pois é do sexo feminino .
          mas caso queira se alistar . ''')

    if idade < 18:
        print(f'Você tem {idade} anos. Ainda faltam {18 - idade} anos para você se alistar.')
        print(f'Seu alistamento será em {ano + 18}.')

    elif idade == 18:
         print(f'Você tem {idade} anos. Está na hora de se alistar!')
         print(f'Seu alistamento será em {ano + 18}.')

    else:
        print(f'Você tem {idade} anos. Já passou do tempo de se alistar há {idade - 18} anos.')
        print(f'Seu alistamento foi em {ano + 18}.')

 continuar = input('\nDeseja consultar outra pessoa? [S/N] ').strip().upper()

 if continuar == 'N':
        print('Programa encerrado.')
        break
   