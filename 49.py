fra = str (input (' qual a frase ? ')) .replace(' ', '') 
fra1 = list(fra)

if fra1 == fra1[::-1]:
    print (' sua frase é um polindromo ')
    
else:
    print (' sua frase não e um polindromo ')