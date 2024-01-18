from .execute_commands import ShowCommand


def show_alerts_suppression_windows(token, format, filter, write):
    alerts_suppression_windows = ShowCommand(token)
    show_alerts_suppression_windows = alerts_suppression_windows(
        "alert-suppression-windows", format, filter, write
    )
    return show_alerts_suppression_windows
