import yaml
import requests
import json
from jinja2 import Environment, FileSystemLoader
from rich.console import Console
from rich import print
import os

console = Console()

os.makedirs("./output", exist_ok=True)


def api_get_data(username, password, call, filter):
    headers = {"content-type": "application/json"}
    url = f"https://api.thousandeyes.com/v6/{call}.json"
    if filter:
        url += f"?aid={filter}"
    try:
        response = requests.get(
            url=url,
            headers=headers,
            auth=(username, password),
        )
        response.raise_for_status()  # Esto generará una excepción si el estado HTTP indica un error
    except requests.HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code == 401:
            return "Error: Unauthorized. Please check your username and password."
        elif status_code == 403:
            return "Error: Forbidden. You do not have the necessary permissions."
        elif status_code == 404:
            return "Error: Not Found. The requested resource could not be found."
        else:
            return f"An HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

    return response.json()


def to_yaml(data, resource, write):
    output = yaml.dump(data)
    if write:
        with open(f"./output/{resource}.yaml", "w") as f:
            f.write(output)
    else:
        console.print(output, style="bold green")


def to_human(data, resource, write):
    file_loader = FileSystemLoader("./templates_human")
    env = Environment(loader=file_loader)
    template = env.get_template(f"{resource}.j2")
    output = template.render(data=data)
    if write:
        with open(f"./output/{resource}.txt", "w") as f:
            f.write(output)
    else:
        console.print(output, style="bold green")


def to_json(data, resource, write):
    output = json.dumps(data, indent=4)
    if write:
        with open(f"./output/{resource}.json", "w") as f:
            f.write(output)
    else:
        console.print(output, style="bold green")


def to_csv(data, resource, write):
    file_loader = FileSystemLoader("./templates_csv")
    env = Environment(loader=file_loader)
    template = env.get_template(f"{resource}.j2")
    output = template.render(data=data)
    if write:
        with open(f"./output/{resource}.csv", "w") as f:
            f.write(output)
    else:
        console.print(output, style="bold green")


def run(username, password, call, format, filter, write, resource):
    data = api_get_data(username, password, call, filter)

    if format == "yaml":
        to_yaml(data, write)
    elif format == "human":
        to_human(data, resource, write)
    elif format == "json" or format is None:
        to_json(data, resource, write)
    elif format == "csv":
        to_csv(data, resource, write)
    else:
        console.print("Format is invalid", style="bold red")

    return ""
