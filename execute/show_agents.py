from .execute_commands import ShowCommand


def show_agents(token, file, aid, write):
    agents = ShowCommand(token)
    show_agents = agents("agents", file, aid, write)
    return show_agents
