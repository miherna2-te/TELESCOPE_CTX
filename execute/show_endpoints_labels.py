from .execute_commands import ShowCommand


def show_endpoints_labels(token, format, filter, write):
    endpoints_labels = ShowCommand(token)
    show_endpoints_labels = endpoints_labels("endpoint/labels", format, filter, write)
    return show_endpoints_labels
