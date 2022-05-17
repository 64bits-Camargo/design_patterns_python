from datetime import datetime
from time import time
import traceback

from observer.subject import Subject
from observer.observer import  Observer


class Invoker:

    def __init__(self, customer, order):
        self.customer = customer
        self.order = order
        self._actions = {}
        self._errors = {}
        self._history = []

    def take_order(self, command_id, command):
        self._actions[command_id] = command

    def place_orders(self):
        send_notify = Subject()
        observer = Observer(send_notify)

        actions_copy_dict = self._actions.copy()
        for command_id, command in actions_copy_dict.items():
            try:
                command.execute()
                self._history.append((time(), command_id))
                print(f'{command_id} --- processed with success!')
            except AttributeError:
                self._errors[command_id] = traceback.format_exception()

        if not self._errors:
            observer.notify(f"Pedido {}")

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
