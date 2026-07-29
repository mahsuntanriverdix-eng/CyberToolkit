from rich.console import Console
from rich.panel import Panel

console = Console()

def show_menu():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]CyberToolkit[/bold cyan]\n"
            "[green]v0.1[/green]"
        )
    )

    console.print("[1] Ağ Araçları")
    console.print("[2] Kriptografi")
    console.print("[3] Sistem Bilgisi")
    console.print("[4] Dosya Araçları")
    console.print("[0] Çıkış")

while True:
    show_menu()

    secim = input("\nSeçiminiz: ")

    if secim == "0":
        console.print("\n[red]Program kapatılıyor...[/red]")
        break

    elif secim == "1":
        input("Ağ Araçları yakında eklenecek...")

    elif secim == "2":
        input("Kriptografi modülü yakında eklenecek...")

    elif secim == "3":
        input("Sistem Bilgisi yakında eklenecek...")

    elif secim == "4":
        input("Dosya Araçları yakında eklenecek...")

    else:
        input("Geçersiz seçim!")