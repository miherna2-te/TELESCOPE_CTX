import re
import sys
from getpass import getpass
import readline
from execute_command import DataProcessor
from rich import print
from rich.console import Console
import socket
from urllib.request import urlopen, URLError
from rich.panel import Panel

console = Console()


def is_valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def is_valid_token(token):
    return len(token) == 32


def check_api_access():
    try:
        socket.gethostbyname("api.thousandeyes.com")
        return True
    except socket.gaierror:
        return False


def parse_command(command_str):
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+filter|\s+format|$)", command_str)
    format = re.search(r"format\s+(yaml|csv|json|human)", command_str)
    write = "write" in command_str
    filter = re.search(r"filter\s+(\d+)", command_str)

    if "format" in command_str and not format:
        raise ValueError(
            "Command incorrect. After 'format' must follow 'yaml', 'csv', 'json', or 'human'."
        )
    if "filter" in command_str and not filter:
        raise ValueError(
            "Command incorrect. After 'filter' must follow a string of numbers."
        )

    resource = resource.group(1).strip() if resource else None
    format = format.group(1) if format else "json"
    filter = filter.group(1) if filter else None

    return resource, format, write, filter


def main():
    welcome_banner = "ThousandEyes: Cortex Welcome"
    console.print(Panel(welcome_banner, border_style="white"), style="bold white")
    username = input("Email: ")
    if not is_valid_email(username):
        console.print("Invalid email, please try again.", style="bold red")
        sys.exit()

    password = getpass("Basic Authentication Token: ")
    if not is_valid_token(password):
        console.print("Invalid token, please try again.", style="bold red")
        sys.exit()

    api_status = "Accessible" if check_api_access() else "Not accessible"
    console.print(f"Welcome, {username}!", style="bold green")
    console.print(f"ThousandEyes API status: {api_status}", style="bold green")
    resources = {
        "tests": "tests.json",
        "accounts": "account-groups.json",
        "tests details": "tests_details.json",
        "endpoints": "endpoint-agents.json",
        "debug": None,
        "ls": None,
    }
    debug_enabled = False
    processor = DataProcessor()
    while True:
        try:
            command_str = input("cortex# ")
            readline.add_history(command_str)

            if not command_str:
                continue

            if command_str.lower() == "ls":
                console.print("\n".join(resources.keys()), style="bold green")
                continue

            if command_str.lower().startswith("show"):
                resource, format, write, filter = parse_command(command_str)

                if resource not in resources:
                    console.print(
                        "Invalid resource. Please use 'tests', 'accounts', 'tests details' or 'endpoints'.",
                        style="bold red",
                    )
                    continue

                call = resources[resource]
                output = processor(username, password, call, format, filter, write, resource)
                console.print(output, style="bold green")

            elif command_str.lower() == "exit":
                break

            if command_str.lower() == "debug enabled":
                debug_enabled = True

            if command_str.lower() == "debug disabled":
                debug_enabled = False

            if debug_enabled:
                console.print(
                    f"{resource=} {call=} {format=}, {write=} {call=} {filter=}",
                    style="bold green",
                )
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    main()
