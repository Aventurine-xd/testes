from datetime import datetime


maior = 0
menor = 0

for c in range (7):
    ano = ( int (input (f' digite o ano de nascimento da {c+1} pessoa : ')))
    idade = datetime.now().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
        
print (f' {maior} pessoas são de maior de idade e {menor} são menores de idade ') 
    
    