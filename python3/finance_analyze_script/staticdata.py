from enum import Enum
from dataclasses import dataclass

SOURCE_DATA_DIR = "SOURCE_DATA_DIR"
FILENAME_PATTERN = "FILENAME_PATTERN"


@dataclass(unsafe_hash=True)
class Spend:
    month: int
    description: str
    code: str
    amount: int


class SpendType(Enum):
    Income = "Income",
    Outcome = "Outcome"


class Person(Enum):
    One = "One"
    Two = "Two"


class CategoryInc(Enum):
    DE1 = "ДЕ1"
    DE2 = "ДЕ2"
    DE3 = "ДЕ3"
    DED = "ДЕД"
    DR1 = "ДР1"
    DR2 = "ДР2"
    DR3 = "ДР3"
    DR4 = "ДР4"
    DR5 = "ДР5"
    DRD = "ДРД"


class CategoryOut(Enum):
    RE1 = "РЕ1"
    RE2 = "РЕ2"
    RE3 = "РЕ3"
    RE4 = "РЕ4"
    RE5 = "РЕ5"
    RE6 = "РЕ6"
    RED = "РЕД"
    RO1 = "РО1"
    RO2 = "РО2"
    RO3 = "РО3"
    RO4 = "РО4"
    ROD = "РОД"
    RP1 = "РП1"
    RP2 = "РП2"
    RP3 = "РП3"
    RP4 = "РП4"
    RP5 = "РП5"
    RPD = "РПД"
    RD1 = "РД1"
    RD2 = "РД2"
    RD3 = "РД3"
    R1 = "Р1"
    R2 = "Р2"
    R3 = "Р3"
    R4 = "Р4"
    R5 = "Р5"
    R6 = "Р6"
    R7 = "Р7"
    R8 = "Р8"
    R9 = "Р9"
    R10 = "Р10"
    R98 = "Р98"
    R99 = "Р99"


all_categories = {
    SpendType.Income: [category.value for category in CategoryInc],
    SpendType.Outcome: [category.value for category in CategoryOut]
}

sheets = {
    Person.One: ["{}".format(x) for x in range(1, 13)],
    Person.Two: ["{}А".format(x) for x in range(1, 13)]
}
