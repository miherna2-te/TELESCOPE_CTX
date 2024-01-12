from .execute_commands import ShowCommand

def show_alerts_rules(token, format, filter, write):
    alerts_rules = ShowCommand(token)
    show_alerts_rules = alerts_rules("alerts/rules", format, filter, write)
    return show_alerts_rules