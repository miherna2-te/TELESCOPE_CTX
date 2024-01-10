import yaml
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from .api_call import api_get_data  # Assuming api_get_data is defined in external_module


class ShowCommand:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.env = Environment(loader=FileSystemLoader("./templates"))

    def __call__(self, resource, format, filter, write):
        data = api_get_data(self.username, self.password, resource, filter)
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
            return "Format is invalid"

        if write:
            with open(f"./output/{resource}_{timestamp}.{format}", "w") as f:
                f.write(output)
                return ""
        return output