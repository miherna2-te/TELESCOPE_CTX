from .execute_commands import ShowCommand

def show_alert_suppression_windows(token, format, filter, write):
    alert_suppression_windows = ShowCommand(token)
    show_alert_suppression_windows = alert_suppression_windows("alert-suppression-windows", format, filter, write)
    return show_alert_suppression_windows