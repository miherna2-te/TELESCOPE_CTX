from .execute_commands import ShowCommand


def show_alerts(token, format, filter, write):
    alerts = ShowCommand(token)
    show_alerts = alerts("alerts", format, filter, write)
    return show_alerts
