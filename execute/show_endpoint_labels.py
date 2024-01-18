from .execute_commands import ShowCommand


def show_endpoint_labels(token, format, filter, write):
    endpoint_labels = ShowCommand(token)
    show_endpoint_labels = endpoint_labels("endpoint/labels", format, filter, write)
    return show_endpoint_labels
