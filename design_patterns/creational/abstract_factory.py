from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

from design_patterns.utils import print_class_meth_name


class Variant(Enum):
    one = "one"
    two = "two"


class VariantFactory(ABC):
    variant: Variant
    sub_variant_one: SubVariant
    sub_variant_two: SubVariant

    @abstractmethod
    def create_sub_variant_one(self):
        pass

    @abstractmethod
    def create_sub_variant_two(self):
        pass


class VariantOneFactory(VariantFactory):

    def __init__(self):
        self.variant = Variant.one
        self.sub_variant_one = SubVariantOne()
        self.sub_variant_two = SubVariantTwo()

    def create_sub_variant_one(self):
        self.sub_variant_one.create(self.variant)

    def create_sub_variant_two(self):
        self.sub_variant_two.create(self.variant)


class VariantTwoFactory(VariantFactory):

    def __init__(self):
        self.variant = Variant.two
        self.sub_variant_one = SubVariantOne()
        self.sub_variant_two = SubVariantTwo()

    def create_sub_variant_one(self):
        self.sub_variant_one.create(self.variant)

    def create_sub_variant_two(self):
        self.sub_variant_two.create(self.variant)


class SubVariant(ABC):
    @abstractmethod
    def create(self, variant: Variant):
        pass


class SubVariantOne(SubVariant):
    @print_class_meth_name()
    def create(self, variant):
        pass


class SubVariantTwo(SubVariant):
    @print_class_meth_name()
    def create(self, variant):
        pass


def run(factory: VariantFactory):
    factory.create_sub_variant_one()
    factory.create_sub_variant_two()


if __name__ == '__main__':
    factory_one = VariantOneFactory()
    run(factory_one)

    factory_two = VariantTwoFactory()
    run(factory_two)
