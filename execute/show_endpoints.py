from .execute_commands import ShowCommand

def show_endpoints(username, password, format, filter, write):
    endpoints = ShowCommand(username, password)
    show_endpoints = endpoints("endpoints", format, filter, write)
    return show_endpoints