from .execute_commands import ShowCommand

def show_agents(token, format, filter, write):
    agents = ShowCommand(token)
    show_agents = agents("agents", format, filter, write)
    return show_agents