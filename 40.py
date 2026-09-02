peso = float (input(' qual e seu peso ? (Kg): '))
alt = float ( input (' qual e a sua altura ?: '))

imc = peso / (alt **2)

if imc < 18.5:
    print ('Abaixo do peso! ')
    
elif 18.5 <= imc <= 24.9:
    print(' peso adequado! ')
    
elif 25 <= imc <= 29.9:
    print ('Sobrepeso! ')
    
elif 30 <= imc <= 34.9:
    print (' Obesidade grau 1! ')
    
elif 35 <= imc <= 39.9:
    print (' Obesidade grau 2! ')
    
else:
    print (' Obesidade grau 3! ')
    
