from __future__ import annotations
from abc import ABC, abstractmethod

from design_patterns.utils import print_class_meth_name, print_callable_name


class SourceAbstraction:

    def __init__(self, source_implementation: SourceImplementation):
        self.source_implementation = source_implementation

    @print_class_meth_name()
    def get_data(self):
        self.source_implementation.source_connect()
        self.source_implementation.source_get()

    @print_class_meth_name("  Sending not allowed")
    def send_data(self):
        pass


class AdvancedSourceAbstraction(SourceAbstraction):

    @print_class_meth_name()
    def get_data(self):
        self.source_implementation.source_connect()
        self.source_implementation.source_get()

    @print_class_meth_name()
    def send_data(self):
        self.source_implementation.source_send()


class SourceImplementation(ABC):
    @abstractmethod
    def source_connect(self):
        pass

    @abstractmethod
    def source_get(self):
        pass

    @abstractmethod
    def source_send(self):
        pass


class SourceFirst(SourceImplementation):
    @print_class_meth_name()
    def source_connect(self):
        pass

    @print_class_meth_name()
    def source_get(self):
        pass

    @print_class_meth_name()
    def source_send(self):
        pass


class SourceSecond(SourceImplementation):
    @print_class_meth_name()
    def source_connect(self):
        pass

    @print_class_meth_name()
    def source_get(self):
        pass

    @print_class_meth_name()
    def source_send(self):
        pass


@print_callable_name()
def run(source_abstraction: SourceAbstraction):
    source_abstraction.get_data()
    source_abstraction.send_data()


if __name__ == '__main__':

    source_first = SourceFirst()
    run(SourceAbstraction(source_first))
    run(AdvancedSourceAbstraction(source_first))

    source_second = SourceSecond()
    run(SourceAbstraction(source_second))
    run(AdvancedSourceAbstraction(source_second))
