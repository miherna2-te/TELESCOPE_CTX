from .execute_commands import ShowCommand

def show_accounts(token, format, filter, write):
    accounts = ShowCommand(token)
    show_accounts = accounts("account-groups", format, filter, write)
    return show_accounts