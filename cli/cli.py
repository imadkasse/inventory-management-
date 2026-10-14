import sys
import os

# إضافة الجذر لمسارات بايثون لتجنب مشاكل الـ ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import typer
from rich.console import Console
from rich.table import Table

# استيراد الخدمات (Services)
from services.category_service import add_category, find_many_category, delete_category
from services.product_service import add_product, find_many_product, delete_product, update_product
from services.transaction_service import add_transaction, find_many_transaction

app = typer.Typer()
console = Console()

def show_main_menu():
    console.print("\n[bold cyan]=== Inventory Management System (IMS) ===[/bold cyan]")
    console.print("[1] Manage Categories")
    console.print("[2] Manage Products")
    console.print("[3] Manage Transactions")
    console.print("[0] Exit")

@app.command()
def interactive():
    """تشغيل النظام كبرنامج تفاعلي متكامل (Interactive TUI)"""
    while True:
        show_main_menu()
        choice = input("\nChoose a section: ").strip()
        
        if choice == "1":
            handle_categories()
        elif choice == "2":
            handle_products()
        elif choice == "3":
            handle_transactions()
        elif choice == "0":
            console.print("[bold blue]Exiting Inventory System. Goodbye! 👋[/bold blue]")
            break
        else:
            console.print("[bold red]Invalid choice, please try again.[/bold red]")

def handle_categories():
    while True:
        console.print("\n[bold yellow]--- Categories Menu ---[/bold yellow]")
        console.print("[1] Add Category")
        console.print("[2] List Categories")
        console.print("[3] Delete Category")
        console.print("[0] Back to Main Menu")
        
        sub_choice = input("Choose option: ").strip()
        if sub_choice == "1":
            name = input("Category Name: ").strip()
            desc = input("Description (optional): ").strip()
            res = add_category(name, desc if desc else None)
            console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "2":
            cats = find_many_category()
            if not cats:
                console.print("[yellow]No categories found.[/yellow]")
                continue
            table = Table(title="Categories", header_style="bold magenta")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Description", style="yellow")
            for c in cats:
                table.add_row(str(c.id), c.name, c.description or "N/A")
            console.print(table)
        elif sub_choice == "3":
            cid = input("Category ID to delete: ").strip()
            if cid.isdigit():
                res = delete_category(int(cid))
                console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "0":
            break

def handle_products():
    while True:
        console.print("\n[bold yellow]--- Products Menu ---[/bold yellow]")
        console.print("[1] Add Product")
        console.print("[2] List Products")
        console.print("[3] Update Product")
        console.print("[4] Delete Product")
        console.print("[0] Back to Main Menu")
        
        sub_choice = input("Choose option: ").strip()
        if sub_choice == "1":
            name = input("Product Name: ").strip()
            price = float(input("Price: ").strip())
            qty = int(input("Quantity: ").strip())
            cat_id = int(input("Category ID: ").strip())
            res = add_product(name, price, qty, cat_id)
            console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "2":
            prods = find_many_product()
            if not prods:
                console.print("[yellow]No products found.[/yellow]")
                continue
            table = Table(title="Products", header_style="bold magenta")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Price", style="blue")
            table.add_column("Qty", style="yellow")
            table.add_column("Category ID", style="magenta")
            for p in prods:
                table.add_row(str(p.id), p.name, str(p.price), str(p.quantity), str(p.category_id))
            console.print(table)
        elif sub_choice == "3":
            pid = int(input("Product ID to update: ").strip())
            new_name = input("New Name (leave blank to skip): ").strip()
            new_price_str = input("New Price (leave blank to skip): ").strip()
            new_qty_str = input("New Quantity (leave blank to skip): ").strip()
            
            res = update_product(
                pid, 
                new_name=new_name if new_name else None,
                new_price=float(new_price_str) if new_price_str else None,
                new_quantity=int(new_qty_str) if new_qty_str else None
            )
            console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "4":
            pid = input("Product ID to delete: ").strip()
            if pid.isdigit():
                res = delete_product(int(pid))
                console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "0":
            break

def handle_transactions():
    while True:
        console.print("\n[bold yellow]--- Transactions Menu ---[/bold yellow]")
        console.print("[1] Add Transaction (IN/OUT)")
        console.print("[2] List Transactions")
        console.print("[0] Back to Main Menu")
        
        sub_choice = input("Choose option: ").strip()
        if sub_choice == "1":
            pid = int(input("Product ID: ").strip())
            t_type = input("Type (IN / OUT): ").upper().strip()
            qty = int(input("Quantity Movement: ").strip())
            notes = input("Notes (optional): ").strip()
            res = add_transaction(pid, t_type, qty, notes if notes else None)
            console.print(f"[bold green]{res}[/bold green]" if "Successfully" in res else f"[bold red]{res}[/bold red]")
        elif sub_choice == "2":
            txs = find_many_transaction()
            if not txs or isinstance(txs, str):
                console.print("[yellow]No transactions found.[/yellow]")
                continue
            table = Table(title="Inventory Transactions", header_style="bold magenta")
            table.add_column("ID", style="cyan")
            table.add_column("Product ID", style="green")
            table.add_column("Type", style="blue")
            table.add_column("Qty", style="yellow")
            table.add_column("Notes", style="white")
            for t in txs:
                table.add_row(str(t.id), str(t.product_id), t.type, str(t.quantity), t.notes or "N/A")
            console.print(table)
        elif sub_choice == "0":
            break

if __name__ == "__main__":
    app()