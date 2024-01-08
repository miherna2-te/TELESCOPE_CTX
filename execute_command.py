import yaml
import requests
import json
from jinja2 import Environment, FileSystemLoader
from rich.console import Console
from rich import print
import os
from datetime import datetime


class DataProcessor:
    def __init__(self):
        self.console = Console()
        os.makedirs("./output", exist_ok=True)

    def api_get_data(self, username, password, call, filter):
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
                return f"An HTTP Error occurred: {http_err}"
        except Exception as err:
            return f"An Error occurred: {err}"

        return response.json()

    def to_yaml(self, data, resource, write):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = yaml.dump(data)
        if write:
            with open(f"./output/{resource}_{timestamp}.yaml", "w") as f:
                f.write(output)
        else:
            self.console.print(output)

    def to_human(self, data, resource, write):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_loader = FileSystemLoader("./templates_human")
        env = Environment(loader=file_loader)
        template = env.get_template(f"{resource}.j2")
        output = template.render(data=data)
        if write:
            with open(f"./output/{resource}_{timestamp}.txt", "w") as f:
                f.write(output)
        else:
            self.console.print(output)

    def to_json(self, data, resource, write):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = json.dumps(data, indent=4)
        if write:
            with open(f"./output/{resource}_{timestamp}.json", "w") as f:
                f.write(output)
        else:
            self.console.print(output)

    def to_csv(self, data, resource, write):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_loader = FileSystemLoader("./templates_csv")
        env = Environment(loader=file_loader)
        template = env.get_template(f"{resource}.j2")
        output = template.render(data=data)
        if write:
            with open(f"./output/{resource}_{timestamp}.csv", "w") as f:
                f.write(output)
        else:
            self.console.print(output)

    def __call__(self, username, password, call, format, filter, write, resource):
        data = self.api_get_data(username, password, call, filter)

        if "Error" in data:
            self.console.print(data, style="bold red")
        elif format == "yaml":
            self.to_yaml(data, resource, write)
        elif format == "human":
            self.to_human(data, resource, write)
        elif format == "json" or format is None:
            self.to_json(data, resource, write)
        elif format == "csv":
            self.to_csv(data, resource, write)
        else:
            self.console.print("Format is invalid", style="bold red")

        return ""
