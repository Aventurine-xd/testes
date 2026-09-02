from datetime import datetime  

while True:
    ano=int(input (' em que ano você neasceu '))

    idade = datetime.now().year - ano

    if idade <= 9:
        print(' voce ainda e mirim: ')  

    elif idade <= 14:
        print (' voce e da categoria infantil: ')

    elif idade <= 19:
        print (' voce e da categoria junior : ') 

    elif idade <= 25:
        print (' voce e da categoria senior: ')
        
    else:
        print (' voce e da categoria master: ')
        
    con = str(input(' voce quer continuar [S/N] ?: ')).strip() .upper()
        
    if con == 'N':
        print('encerrando... ')
        break      