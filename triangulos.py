from rich.console import Console

console = Console()

num1 = float(console.input("[bold blue]Digite o primeiro número: [bold white]"))
num2 = float(console.input("[bold blue]Digite o segundo número: [bold white]"))
num3 = float(console.input("[bold blue]Digite o terceiro número: [bold white]"))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    console.print(
        f"[bold blue]Os segmentos [bold white]{num1:.1f}[/bold white], [bold white]{num2:.1f}[/bold white] e [bold white]{num3:.1f}[/bold white] [bold blue]PODEM formar um triângulo![/bold blue]"
    )
    
    if num1 == num2 and num2 == num3:
     console.print (' [bold green]seu triangulo e equilatero ')
    
    elif num1 == num2 or num2 == num3 or num1 == num3 :
     console.print ('[bold green] seu triangulo e isosceles ')
    
    else:
     console.print('[bold green] seu triangulo e escaleno ')

else:
    console.print(
        f"[bold blue]Os segmentos [bold white]{num1:.1f}[/bold white], [bold white]{num2:.1f}[/bold white] e [bold white]{num3:.1f}[/bold white] [bold blue]NÃO PODEM formar um triângulo![/bold blue]"
    )