from .execute_commands import ShowCommand


def show_bgp_monitors(token, format, filter, write):
    bgp_monitors = ShowCommand(token)
    show_bgp_monitors = bgp_monitors("monitors", format, filter, write)
    return show_bgp_monitors
