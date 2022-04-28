class Invoker:
    _actions = []

    def take_order(self, product):
        self._actions.append(product)

    def place_orders(self):
        loading = '.'
        for index, product in enumerate(self._actions):
            loading += '. OK!' \
                if index == (len(self._actions) - 1) else '.'
            print(f'process {loading}')

            product.execute()

        self._actions.clear()
