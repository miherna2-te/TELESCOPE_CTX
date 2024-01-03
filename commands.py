import os
import importlib
from rich.console import Console

console = Console()


class CommandHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def execute_command(self, command, format, account_groups):
        pass
