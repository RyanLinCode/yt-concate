from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    # inputs 用字典打包避免一直增加參數卻只有某一個step用得到
    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass
