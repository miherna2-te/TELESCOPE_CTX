import yaml
import requests
import json
from jinja2 import Environment, FileSystemLoader
from rich.console import Console
import os
from datetime import datetime


class DataProcessor:
    def __init__(self):
        self.console = Console()
        os.makedirs("./output", exist_ok=True)
        self.env = Environment(loader=FileSystemLoader("./templates"))

    def api_get_data(self, username, password, call, filter):
        url = f"https://api.thousandeyes.com/v6/{call}.json"
        if filter:
            url += f"?aid={filter}"
        try:
            response = requests.get(
                url=url,
                headers={"content-type": "application/json"},
                auth=(username, password),
            )
            response.raise_for_status()
        except requests.HTTPError as http_err:
            return f"An HTTP Error occurred: {http_err}"
        except Exception as err:
            return f"An Error occurred: {err}"
        return response.json()

    def to_file(self, data, resource, format, write):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = ""
        if format == "json":
            output = json.dumps(data, indent=4)
        elif format in ["yaml", "csv", "human"]:
            if format == "yaml":
                output = yaml.dump(data)
            else:
                template = self.env.get_template(f"{resource}_{format}.j2")
                output = template.render(data=data)
        else:
            self.console.print("Format is invalid", style="bold red")
            return

        if write:
            with open(f"./output/{resource}_{timestamp}.{format}", "w") as f:
                f.write(output)
        else:
            self.console.print(output)

    def __call__(self, username, password, call, format, filter, write, resource):
        data = self.api_get_data(username, password, call, filter)
        if "Error" in data:
            self.console.print(data, style="bold red")
        else:
            self.to_file(data, resource, format or "json", write)
        return ""
