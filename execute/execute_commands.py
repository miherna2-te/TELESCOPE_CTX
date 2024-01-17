import yaml
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from .api_call import (
    api_get_data,
)  # Assuming api_get_data is defined in external_module


class ShowCommand:
    def __init__(self, token):
        self.token = token
        self.env = Environment(loader=FileSystemLoader("./templates"))

    def __call__(self, resource, format, filter, write):
        data = api_get_data(self.token, resource, filter)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output = ""
        if format == "json":
            output = json.dumps(data, indent=4)
        elif format in ["yaml", "csv", "human"]:
            if format == "yaml":
                output = yaml.dump(data)
            else:
                resource_file = resource.replace("/", "_").replace("-", "_")
                template = self.env.get_template(f"{resource_file}_{format}.j2")
                output = template.render(data=data)
        else:
            return "Format is invalid"

        if write:
            resource_file = resource.replace("/", "_").replace("-", "_")
            with open(f"./output/{resource_file}_{timestamp}.{format}", "w") as f:
                f.write(output)
                return f"File created: ./output/{resource_file}_{timestamp}.{format}"
        return output
