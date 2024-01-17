import requests


def api_get_data(token, resource, filter):
    url = f"https://api.thousandeyes.com/v7/{resource}"
    if filter:
        url += f"?aid={filter}"
    try:
        response = requests.get(
            url=url,
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            return "Error: Unauthorized. Check your credentials."
        elif response.status_code == 403:
            return "Error: Forbidden. You don't have the necessary permissions."
        elif response.status_code == 404:
            return f"Error: Not Found. The resource {resource} was not found."
        elif response.status_code == 429:
            return "Error: Too Many Requests. You've hit the rate limit."
        else:
            return f"An HTTP Error occurred: {http_err}"
    except Exception as err:
        return f"An Error occurred: {err}"
    return response.json()
