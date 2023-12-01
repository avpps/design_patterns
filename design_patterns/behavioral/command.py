from __future__ import annotations
from abc import ABC, abstractmethod

from design_patterns.utils import print_class_meth_name


class CommandDesc:

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class Receiver:

    def do_one(self):
        pass

    def do_another(self):
        pass


class Command(ABC):

    @abstractmethod
    def do(self):
        pass


class OnActionCommand(Command):

    @print_class_meth_name()
    def do(self):
        pass


class OnEndCommand(Command):

    @print_class_meth_name()
    def do(self):
        pass


class Dispatcher:
    on_action = CommandDesc()
    on_end = CommandDesc()

    def __init__(self, on_action: Command, on_end: Command):
        self.on_action = on_action
        self.on_end = on_end

    def action(self):
        # TODO: How to pass args to commands
        self.on_action.do()
        print(f"Action in {self.__class__.__name__}")
        self.on_end.do()


if __name__ == '__main__':
    dispatcher = Dispatcher(on_action=OnActionCommand(), on_end=OnEndCommand())
    dispatcher.action()
