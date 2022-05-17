from abc import ABC, abstractmethod


class IObserver(ABC):

    @staticmethod
    @abstractmethod
    def notify(): ...


class Observer(IObserver):

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, *args):
        print(f"Observer id:{id(self)} received {args}")
