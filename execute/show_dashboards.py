from .execute_commands import ShowCommand


def show_dashboards(token, format, filter, write):
    dashboards = ShowCommand(token)
    show_dashboards = dashboards("dashboards", format, filter, write)
    return show_dashboards
