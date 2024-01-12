from .execute_commands import ShowCommand

def show_endpoints(token, format, filter, write):
    endpoints = ShowCommand(token)
    show_endpoints = endpoints("endpoint/agents", format, filter, write)
    return show_endpoints