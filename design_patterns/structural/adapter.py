from __future__ import annotations

from design_patterns.utils import print_class_meth_name, print_callable_name


class Requester:
    @print_class_meth_name()
    def request(self):
        pass


class LegacyRequester:
    @print_class_meth_name()
    def legacy_request(self):
        pass


class LegacyRequesterAdapter(Requester, LegacyRequester):
    @print_class_meth_name()
    def request(self):
        super().legacy_request()


@print_callable_name("\n")
def run(requester: Requester):
    requester.request()


if __name__ == '__main__':
    run(Requester())
    run(LegacyRequesterAdapter())
