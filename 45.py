from rich.console import Console
from rich import print

console = Console()

soma = 0

for n in range (3, 501, 6):
    soma = soma + n
    
print (f'[bold green] O valor da soma dos numeros impares e de {soma}')    