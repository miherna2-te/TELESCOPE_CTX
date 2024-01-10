from .execute_commands import ShowCommand

def show_accounts(username, password, format, filter, write):
    accounts = ShowCommand(username, password)
    show_accounts = accounts("account-groups", format, filter, write)
    return show_accounts