from rich.console import Console
from rich.panel import Panel

# Inicializa o console do Rich
console = Console()

def calcular_reajuste():
    # Painel de destaque para o título
    console.print(Panel.fit("[bold yellow]Calculadora de Reajuste Salarial[/bold yellow]", border_style="blue"))
    
    # Loop de validação de entrada (previne erros se o usuário digitar vírgula, letras ou deixar vazio)
    while True:
        entrada = console.input("[bold]Qual é o seu salário? R$ [/bold]").strip().replace(",", ".")
        try:
            salario = float(entrada)
            if salario <= 0:
                console.print("[bold red]Por favor, digite um valor de salário maior que zero.[/bold red]")
                continue
            break
        except ValueError:
            console.print("[bold red]Entrada inválida! Digite apenas números (ex: 1200 ou 1500.50).[/bold red]")

    # Regra de negócio:
    # Salários até R$ 1.250,00 -> 15% de aumento
    # Salários acima de R$ 1.250,00 -> 10% de aumento
    porcentagem = 15 if salario <= 1250 else 10
    aumento = salario * (porcentagem / 100)
    novo_salario = salario + aumento

    # Exibição dos resultados com tags Rich devidamente fechadas e f-strings
    console.print(
        f"\n[bold green][+] Reajuste calculado com sucesso![/bold green]\n"
        f"  - Salário anterior : [bold white]R$ {salario:.2f}[/bold white]\n"
        f"  - Aumento aplicado : [bold yellow]{porcentagem}%[/bold yellow] ([bold cyan]+ R$ {aumento:.2f}[/bold cyan])\n"
        f"  - Novo salário     : [bold green]R$ {novo_salario:.2f}[/bold green]"
    )

if __name__ == "__main__":
    calcular_reajuste()
