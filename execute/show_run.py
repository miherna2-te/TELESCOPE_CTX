from rich.console import Console
from rich.table import Table

console = Console()


def show_run(token, debug_enabled, api_status):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Field", style="dim", width=20)
    table.add_column("Value")
    table.add_row("Bearer Token", "********" + token[28:])
    table.add_row("Debug", str(debug_enabled))
    table.add_row("API Status", api_status)
    table.add_row("API Version:", "V7")

    console.print(table)
    return ""
