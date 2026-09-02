par = 0

for i in range (1, 7):
    n = int(input(f' qual o valor do {i} numero? '))
    if n % 2 == 0 :
      par = par + n 

print (f' a soma dos numeros pares e de {par} ')
