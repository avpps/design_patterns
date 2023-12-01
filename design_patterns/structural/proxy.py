from abc import ABC, abstractmethod
from design_patterns.utils import print_class_meth_name


class BaseWorker(ABC):
    @abstractmethod
    def do(self):
        pass


class ProxyWorker(BaseWorker):

    @print_class_meth_name("something")
    def do(self):
        RealWorker().do()


class RealWorker(BaseWorker):

    @print_class_meth_name()
    def do(self):
        pass


def run(worker: BaseWorker):
    worker.do()


if __name__ == '__main__':
    worker = ProxyWorker()
    run(worker=worker)
