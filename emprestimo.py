from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.progress import track
console = Console()


casa = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o valor do seu salário: "))
ano = int(input("Digite em quantos anos você quer pagar: "))

prestacao = casa / (ano * 12)
minimo = salario * 0.3  

if prestacao <= minimo:
    table = Table(title="Resultado do Empréstimo")
    table.add_column("Status", style="bold red")
    table.add_column("Valor da Casa", style="bold blue")
    table.add_column("Prestação Mensal", style="bold magenta")
    table.add_column("Prazo", style="bold cyan")
    table.add_row("Recusado", f"R${casa:.2f}", f"R${prestacao:.2f}", f"{ano} anos")
    console.print(table)
    
else:
    table = Table(title="Resultado do Empréstimo")
    table.add_column("Status", style="bold red")
    table.add_column("Valor da Casa", style="bold blue")
    table.add_column("Prestação Mensal", style="bold magenta")
    table.add_column("Prazo", style="bold cyan")
    table.add_row("Negado", f"R${casa:.2f}", f"R${prestacao:.2f}", f"{ano} anos")
    console.print(table)