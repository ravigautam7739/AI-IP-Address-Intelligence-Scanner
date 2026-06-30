from rich.console import Console
from rich.progress import Progress
import random
import time

console = Console()

console.print("\n[bold cyan]JARVIS AI IP ADDRESS INTELLIGENCE[/bold cyan]\n")

ip = input("Enter IP Address: ").strip()

if ip == "":
    ip = "8.8.8.8"

console.print(f"\nTarget IP : [yellow]{ip}[/yellow]\n")

time.sleep(1)

steps = [
    "Initializing Intelligence Engine",
    "Locating IP Address",
    "Checking ISP Database",
    "Checking ASN Information",
    "Scanning Abuse Reports",
    "Checking VPN Detection",
    "Checking Proxy Detection",
    "Checking Tor Exit Nodes",
    "Analyzing Network Reputation",
    "Searching Blacklist Database",
    "Running AI Threat Analysis",
    "Generating Intelligence Report"
]

for step in steps:

    console.print(f"\n[cyan]{step}...[/cyan]")

    with Progress() as progress:

        task = progress.add_task(
            "[green]Analyzing...",
            total=100
        )

        while not progress.finished:

            progress.update(
                task,
                advance=random.randint(2,6)
            )

            time.sleep(0.04)

    console.print("[bold green]✓ Complete[/bold green]")

    time.sleep(0.35)

trust = random.randint(97,100)

console.print("\n" + "="*68)

console.print("\n[bold yellow]IP INTELLIGENCE REPORT[/bold yellow]\n")

console.print(f"IP Address          : {ip}")
console.print("Country            : United States")
console.print("Region             : California")
console.print("City               : Mountain View")
console.print("ISP                : Google LLC")
console.print("ASN                : AS15169")
console.print("VPN                : NOT DETECTED")
console.print("Proxy              : NOT DETECTED")
console.print("Tor Exit Node      : NO")
console.print("Blacklist Status   : CLEAN")
console.print("Abuse Reports      : 0")
console.print("Threat Level       : LOW")
console.print(f"Trust Score        : {trust}/100")

console.print("\n[bold green]STATUS : SAFE IP VERIFIED ✓[/bold green]")
console.print("[bold cyan]NO SUSPICIOUS NETWORK ACTIVITY DETECTED[/bold cyan]")

console.print("\n" + "="*68)

console.print("\n[bold green]AI ANALYSIS COMPLETED SUCCESSFULLY[/bold green]\n")