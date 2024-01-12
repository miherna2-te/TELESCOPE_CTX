from execute.show_accounts import show_accounts
from execute.show_agents import show_agents
from execute.show_alert_suppression_windows import show_alert_suppression_windows
from execute.show_alerts import show_alerts
from execute.show_alerts_rules import show_alerts_rules
from execute.show_endpoints import show_endpoints
from execute.show_run import show_run
from execute.show_tests import show_tests
from getpass import getpass
from rich import print, console, panel
import os
import re
import readline
import socket
import sys

console = console.Console()


def parse_command(command_str):
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+aid|\s+format|$)", command_str)
    format = re.search(r"format\s+(yaml|csv|json|human)", command_str)
    aid = re.search(r"aid\s+(\d+)", command_str)
    return (
        resource and resource.group(1).strip(),
        format and format.group(1) or "json",
        aid and aid.group(1) or None,
        "write" in command_str,
    )


def get_match(string, pattern):
    match = re.search(pattern, string)
    return match.group(1).strip() if match else None


def validate_credentials(token):
    if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", token):
        console.print("Error: Invalid Bearer token, please try again.", style="bold red")
        sys.exit()

def main():
    os.makedirs("./output", exist_ok=True)
    console.print(
        panel.Panel("ThousandEyes/Telescope Welcome", border_style="orange_red1"),
        style="orange_red1",
    )

    token = os.environ.get('TELESCOPE_BEARER') or getpass("Bearer Authentication Token: ")
    api_status = (
        "Accessible"
        if socket.gethostbyname("api.thousandeyes.com")
        else "Not accessible"
    )
    console.print(f"Welcome to ThousandEyes!\nThousandEyes API status: {api_status}")

    resources = {
        "accounts": show_accounts,
        "alert suppression windows": show_alert_suppression_windows,
        "alerts": show_alerts,
        "alerts rules": show_alerts_rules,
        "agents": show_agents,
        "endpoints": show_endpoints,
        "run": show_run,
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
            resource, format, aid, write = parsed_command
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
                output = show_run(token, debug_enabled, api_status)
                console.print(output)
            elif command == "show" and resource in resources:
                output = resources[resource](token, format, aid, write)
                if "Error" in output:
                    output = output.replace("\"", "")
                    console.print(output, style="bold red")
                else:
                    console.print(output)
                if debug_enabled:
                    console.print(f"{resource=} {format=}, {aid=}  {write=}")
            elif command == "exit":
                break
            else:
                console.print(f"Invalid command. Please try again.", style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    main()
