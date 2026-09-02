import time
from rich.console import Console
from rich import print

Console = Console()

for c in range (10, -1, -1):
    time.sleep(1)
    print(c)

print('[bold green] FOGOS ')
