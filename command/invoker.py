from datetime import datetime
from time import time
import traceback


class Invoker:

    def __init__(self):
        self._actions = {}
        self._errors = {}
        self._history = []

    def take_order(self, command_id, command):
        self._actions[command_id] = command

    def place_orders(self):
        actions_copy_dict = self._actions.copy()
        for command_id, command in actions_copy_dict.items():
            try:
                command.execute()
                self._history.append((time(), command_id))
                print(f'{command_id} --- processed with success!')
            except AttributeError:
                self._errors[command_id] = traceback.format_exception()

    def show_history(self):
        for row in self._history:
            print(
                f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')}"
                f" : {row[1]}"
            )

    def reprocess_last_place_orders(self, number_of_commands=None):
        if number_of_commands is None:
            number_of_commands = len(self._history)
        commands = self._history[-number_of_commands:]
        for command in commands:
            self._actions[command[1]].execute()
