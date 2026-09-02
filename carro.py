kh=float(input('quantos km/h voce esta dirigindo? '))
if kh > 80:
    print(' voce esta acima da velocidade permitida, MULTADO ! ')
    multa = (kh - 80) * 7
    print(' voce deve pagar uma multa de R$ ', multa)   
else:
    print(' voce esta dentro da velocidade permitida, continue assim ! ')