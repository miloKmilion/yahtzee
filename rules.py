from hand import Hand
from abc import abstractmethod, ABC  # To define the kind of rule it is.


class Rule(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def points(self, hand: Hand):
        pass


class SameValueRule(Rule):
    def __init__(self, value: int, name: str):
        self.__value = value
        self.__name = name

    def name(self):
        return self.__name

    def points(self, hand: Hand):
        return hand.count(self.__value) * self.__value

