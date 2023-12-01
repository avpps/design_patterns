from __future__ import annotations
from abc import ABC, abstractmethod

from design_patterns.utils import print_class_meth_name


class Context:
    state: State

    def __init__(self, initial_state: State):
        self.set_state(initial_state)

    def set_state(self, state):
        self.state = state
        self.state.context = self

    def do_first(self, params):
        self.state.act_first(params)

    def do_sec(self, params):
        self.state.act_sec(params)


class State(ABC):
    context: Context

    @abstractmethod
    def act_first(self, params):
        pass

    @abstractmethod
    def act_sec(self, params):
        pass


class StateOne(State):

    @print_class_meth_name
    def act_first(self, params):
        self.context.set_state(StateTwo())

    @print_class_meth_name
    def act_sec(self, params):
        pass


class StateTwo(State):

    @print_class_meth_name
    def act_first(self, params):
        self.context.set_state(StateOne())

    @print_class_meth_name
    def act_sec(self, params):
        pass


def run():
    initial_state = StateOne()
    ctx = Context(initial_state=initial_state)
    ctx.do_first("fff")
    ctx.do_sec("sss")
    ctx.do_first("fff")
    ctx.do_sec("sss")


if __name__ == '__main__':
    run()
