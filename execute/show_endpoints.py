import yaml
import requests
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def api_get_data(username, password, filter):
    url = f"https://api.thousandeyes.com/v6/endpoint-agents.json.json"
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


def show_endpoints(username, password, format, filter, write):
    data = api_get_data(username, password, filter)
    env = Environment(loader=FileSystemLoader("./templates"))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output = ""
    if format == "json":
        output = json.dumps(data, indent=4)
    elif format in ["yaml", "csv", "human"]:
        if format == "yaml":
            output = yaml.dump(data)
        else:
            template = env.get_template(f"endpoints_{format}.j2")
            output = template.render(data=data)
    else:
        return "Format is invalid"

    if write:
        with open(f"./output/endpoints_{timestamp}.{format}", "w") as f:
            f.write(output)
    return output
