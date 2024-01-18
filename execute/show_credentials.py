from .execute_commands import ShowCommand


def show_credentials(token, format, filter, write):
    credentials = ShowCommand(token)
    show_credentials = credentials("credentials", format, filter, write)
    return show_credentials
