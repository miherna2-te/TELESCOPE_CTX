import re
import sys
from getpass import getpass
import readline
from execute_command import run


def is_valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def is_valid_token(token):
    return len(token) == 32


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

    resource = resource.group(1) if resource else None
    format = format.group(1) if format else "json"
    filter = filter.group(1) if filter else None

    return resource, format, write, filter


def main():
    username = input("Email: ")
    if not is_valid_email(username):
        print("Invalid email, please try again.")
        sys.exit()

    password = getpass("Basic Authentication Token: ")
    if not is_valid_token(password):
        print("Invalid token, please try again.")
        sys.exit()

    resources = ["show tests", "show accounts", "show tests details"]

    while True:
        try:
            command_str = input("cortex# ")
            readline.add_history(command_str)

            if not command_str:
                continue

            if command_str.lower() == "ls":
                print("\n".join(resources))
                continue

            if command_str.lower().startswith("show"):
                resource, format, write, filter = parse_command(command_str)

                # Set command based on resource
                match resource:
                    case "tests":
                        call = "tests.json"
                    case "accounts":
                        call = "account-groups.json"
                    case "tests details":
                        call = "tests_details.json"
                    case _:
                        print(
                            "Invalid resource. Please use 'tests', 'accounts' or 'tests details'."
                        )
                        continue

            elif command_str.lower() == "exit":
                break

            print(
                f"{resource=}, {filter=}, {call=}, {format=}, {write=} {call=} {filter=}"
            )
            output = run(username, password, call, format, filter, write, resource)
            print(output)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
