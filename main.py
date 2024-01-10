import os
import re
import readline
import socket
import sys
from getpass import getpass
from rich import print, console, panel
from execute.show_run import show_run
from execute.show_accounts import show_accounts
from execute.show_endpoints import show_endpoints
from execute.show_tests import show_tests

console = console.Console()


def parse_command(command_str):
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+filter|\s+format|$)", command_str)
    format = re.search(r"format\s+(yaml|csv|json|human)", command_str)
    filter = re.search(r"filter\s+(\d+)", command_str)
    return (
        resource and resource.group(1).strip(),
        format and format.group(1) or "json",
        filter and filter.group(1) or None,
        "write" in command_str,
    )


def get_match(string, pattern):
    match = re.search(pattern, string)
    return match.group(1).strip() if match else None


def validate_credentials(username, password):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", username):
        console.print("Error: Invalid email, please try again.", style="bold red")
        sys.exit()
    if len(password) != 32:
        console.print("Error: Invalid token, please try again.", style="bold red")
        sys.exit()


def main():
    os.makedirs("./output", exist_ok=True)
    console.print(
        panel.Panel("ThousandEyes/Telescope Welcome", border_style="orange_red1"),
        style="orange_red1",
    )
    username = os.environ.get('TELESCOPE_USER') or input("Email: ")
    password = os.environ.get('TELESCOPE_PWD') or getpass("Basic Authentication Token: ")
    api_status = (
        "Accessible"
        if socket.gethostbyname("api.thousandeyes.com")
        else "Not accessible"
    )
    console.print(f"Welcome, {username}!\nThousandEyes API status: {api_status}")
    resources = {
        "run": show_run,
        "accounts": show_accounts,
        "endpoints": show_endpoints,
        "tests": show_tests,
    }
    debug_enabled = False
    while True:
        try:
            command_str = input("telescope# ").lower()
            readline.add_history(command_str)
            command_parts = command_str.split()
            command = command_parts[0] if command_parts else None
            parsed_command = parse_command(command_str)
            resource, format, filter, write = parsed_command
            if command_str == "":
                continue
            elif command_str == "debug enabled":
                debug_enabled = True
                continue
            elif command_str == "debug disabled":
                debug_enabled = False
                continue
            if command == "!":
                continue
            elif command == "ls":
                show_files = [
                    os.path.splitext(file)[0].replace("_", " ")
                    for file in os.listdir("execute")
                    if "show" in file
                ]
                console.print("\n".join(show_files), style="bold green")
            elif command == "show" and resource == "run":
                output = show_run(username, password, debug_enabled, api_status)
                console.print(output)
            elif command == "show" and resource in resources:
                output = resources[resource](username, password, format, filter, write)
                if "Error" in output:
                    output = output.replace("\"", "")
                    console.print(output, style="bold red")
                else:
                    console.print(output)
                if debug_enabled:
                    console.print(f"{resource=} {format=}, {filter=}  {write=}")
            elif command == "exit":
                break
            else:
                console.print(f"Invalid command. Please try again.", style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    main()
