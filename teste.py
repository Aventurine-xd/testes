a = int(input('Digite um numero '))
b = int(input('Digite outro numero '))
c = int(input('Digite mais um numero '))
maior = a
if b>a and b>c:
    maior = b
elif c>a and c>b:
    maior = c

    menor = a 
if b<a and b<c:
    menor =b 
elif c<a and c<b:
    menor = c 
print (' o maior numero digitado foi {} ' . format(maior))
print(' o menor numero digitada foiu {} ' .format(menor))
