import os
import re
import socket
from getpass import getpass
import importlib
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from rich import print, console, panel

console = console.Console()

# Constant for the execute directory
EXECUTE_DIRECTORY = "./execute"

# Function to parse the command string
def parse_command(command_str):
    resource = re.search(r"show\s+(.*?)(?=\s+write|\s+aid|\s+file|$)", command_str)
    file_format = re.search(r"file\s+(yaml|csv|json|human)", command_str)
    aid = re.search(r"aid\s+(\d+)", command_str)
    return (
        resource and resource.group(1).strip(),
        file_format and file_format.group(1) or "json",
        aid and aid.group(1) or None,
        "write" in command_str,
    )


# Function to show available resources
def execute_show_resources():
    show_files = [
        os.path.splitext(file)[0].replace("_", " ")
        for file in os.listdir(EXECUTE_DIRECTORY)
        if "show" in file
    ]
    return sorted(show_files)


commands_list = execute_show_resources()

# Function to get commands from the execute directory
def show_commands_in_directory():
    commands = {}
    for file in os.listdir(EXECUTE_DIRECTORY):
        if "show" in file:
            key = file.replace("show_", "").replace(".py", "").replace("_", " ")
            value = f"execute.{file.replace('.py', '')}"
            commands[key] = value
    return commands


# Main function
def main():
    os.makedirs("./output", exist_ok=True)
    api_status = (
        "Accessible"
        if socket.gethostbyname("api.thousandeyes.com")
        else "Not accessible"
    )

    console.print(
        panel.Panel(
            f"ThousandEyes/Telescope Welcome. API Status: {api_status}",
            border_style="orange_red1",
        ),
        style="orange_red1",
    )
    token = os.environ.get("TELESCOPE_BEARER") or getpass(
        "Bearer Authentication Token: "
    )

    show_commands = show_commands_in_directory()

    debug_enabled = False
    while True:
        try:
            command_str = (
                prompt("telescope# ", history=FileHistory("history.txt"))
                .lower()
                .strip()
            )
            command_parts = command_str.split()
            command = command_parts[0] if command_parts else None
            resource, file_format, aid, write = parse_command(command_str)
            if command_str == "":
                continue
            elif command_str == "debug enabled":
                debug_enabled = True
                continue
            elif command_str == "debug disabled":
                debug_enabled = False
                continue
            elif command in ["!", "#"]:
                continue
            elif command == "ls" or (command == "show" and resource is None):
                print("\n".join(commands_list))
            elif command == "show" and resource == "run":
                module = importlib.import_module(show_commands[resource])
                function_name = "show_" + resource.replace(" ", "_")
                function = getattr(module, function_name, None)
                output = function(token, debug_enabled, api_status)
                console.print(output)
            elif command == "show" and resource in show_commands:
                module = importlib.import_module(show_commands[resource])
                function_name = "show_" + resource.replace(" ", "_")
                function = getattr(module, function_name, None)
                output = function(token, file_format, aid, write)
                if "Error" in output:
                    console.print(output.replace('"', ""), style="bold red")
                else:
                    console.print(output)
                if debug_enabled:
                    console.print(f"{resource=} {file_format=}, {aid=}  {write=}")
            elif command == "exit":
                break
            else:
                console.print("Invalid command. Please try again.", style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    main()
