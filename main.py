import re
import sys
import socket
import readline
from getpass import getpass
from execute_command import DataProcessor
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()


def parse_command(command_str):
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+filter|\s+format|$)", command_str)
    format = re.search(r"format\s+(yaml|csv|json|human)", command_str)
    return (
        resource and resource.group(1).strip(),
        format and format.group(1) or "json",
        "write" in command_str,
        re.search(r"filter\s+(\d+)", command_str),
    )


def main():
    console.print(
        Panel("ThousandEyes/Telescope Welcome", border_style="orange_red1"),
        style="orange_red1",
    )

    username = input("Email: ")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", username):
        console.print("Error: Invalid email, please try again.", style="bold red")
        sys.exit()

    password = getpass("Basic Authentication Token: ")
    if len(password) != 32:
        console.print("Error: Invalid token, please try again.", style="bold red")
        sys.exit()

    api_status = (
        "Accessible"
        if socket.gethostbyname("api.thousandeyes.com")
        else "Not accessible"
    )
    console.print(f"Welcome, {username}!\nThousandEyes API status: {api_status}")
    resources = {
        "tests": "tests.json",
        "accounts": "account-groups.json",
        "tests details": "tests_details.json",
        "endpoints": "endpoint-agents.json",
    }
    processor = DataProcessor()
    debug_enabled = False
    while True:
        try:
            command_str = input("cortex# ")
            readline.add_history(command_str)
            if not command_str or command_str.lower() == "ls":
                console.print(
                    "\n".join([f"show {cmd}" for cmd in resources.keys()]),
                    style="bold green",
                )
                continue
            if command_str.lower() == "show run":
                console.print(f" Username: {username}")
                console.print(f" Password: {password}")
                console.print(f" Debug: {debug_enabled}")
                console.print(f" API Status: {api_status}")
            elif command_str.lower().startswith("show"):
                resource, format, write, filter = parse_command(command_str)
                if resource not in resources:
                    console.print(
                        f"Invalid resource. Please use: {', '.join(resources.keys())}",
                        style="bold red",
                    )
                    continue
                call = resources[resource]
                output = processor(
                    username, password, call, format, filter, write, resource
                )
                if debug_enabled:
                    console.print(
                        f"{resource=} {call=} {format=}, {write=} {call=} {filter=}"
                    )
            elif command_str.lower() == "exit":
                break
            elif command_str.lower() in ["debug enabled", "debug disabled"]:
                debug_enabled = command_str.lower() == "debug enabled"
            else:
                console.print(
                            f"Invalid resource. Please use: {', '.join(resources.keys())}",
                            style="bold red",
                        )
                continue
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    main()
