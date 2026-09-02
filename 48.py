n = int ( input (' qual numero deseja analisar? '))
va = 0


for c in range (2, n +1 ):
   va1 = n % c 
   if va1 == 0:
       va = va + 1
       
if va == 1:
    print (f' {n} é um numero primo ') 
    
else: 
    print ( f' {n} não e um numero primo ')