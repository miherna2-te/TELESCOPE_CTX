from .execute_commands import ShowCommand


def show_accounts(token, file, aid, write):
    accounts = ShowCommand(token)
    show_accounts = accounts("account-groups", file, aid, write)
    return show_accounts
