import os
import re
import readline
import socket
import sys
from getpass import getpass
from rich import print, console, panel
import importlib

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


def validate_credentials(token):
    if not re.match(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", token
    ):
        console.print(
            "Error: Invalid Bearer token, please try again.", style="bold red"
        )
        sys.exit()


def main():
    os.makedirs("./output", exist_ok=True)
    console.print(
        panel.Panel("ThousandEyes/Telescope Welcome", border_style="orange_red1"),
        style="orange_red1",
    )

    token = os.environ.get("TELESCOPE_BEARER") or getpass(
        "Bearer Authentication Token: "
    )
    api_status = (
        "Accessible"
        if socket.gethostbyname("api.thousandeyes.com")
        else "Not accessible"
    )
    console.print(f"Welcome to ThousandEyes!\nThousandEyes API status: {api_status}")

    show_commands = {}
    for file in os.listdir("./execute"):
        if "show" in file:
            key = file.replace("show_", "").replace(".py", "").replace("_", " ")
            value = f"execute.{file.replace('.py', '')}"
            show_commands[key] = value

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
            if command == "!" or command == "#":
                continue
            elif command == "ls" or (command == "show" and resource is None):
                show_files = [
                    os.path.splitext(file)[0].replace("_", " ")
                    for file in os.listdir("execute")
                    if "show" in file
                ]
                print("\n".join(show_files))
            elif command == "show" and resource == "run":
                module = importlib.import_module(show_commands[resource])
                output = module.show_run(token, debug_enabled, api_status)
                print(output)
            elif command == "show" and resource in show_commands:
                module = importlib.import_module(show_commands[resource])
                function_name = "show_" + resource.replace(" ", "_")
                function = getattr(module, function_name, None)
                output = function(token, format, aid, write)
                if "Error" in output:
                    output = output.replace('"', "")
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
