nome= input("Digite seu nome: ")

equacao= input("Digite a equação que deseja resolver (ex: - + * /): ")

val1= float(input("Digite o primeiro valor: "))
val2= float(input("Digite o segundo valor: "))

if equacao == "+":
    resultado = val1 + val2
elif equacao == "-":
    resultado = val1 - val2
elif equacao == "*":
    resultado = val1 * val2
elif equacao == "/":
    resultado = val1 / val2

print("{0} {1}, O resultado de {2} {3} {4} é {5}".format(nome, val1, equacao, val2, resultado))
