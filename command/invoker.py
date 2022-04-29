import traceback

class Invoker:

    def __init__(self):
        self._actions = {}
        self._errors = {}

    def take_order(self, command_id, command):
        self._actions[command_id] = command

    def place_orders(self):
        actions_copy_dict = self._actions.copy()
        for command_id, command in actions_copy_dict.items():
            try:
                command.execute()
                print(f'{command_id} --- processed with success!')
                del self._actions[command_id]
            except AttributeError:
                self._errors[command_id] = traceback.format_exception()
