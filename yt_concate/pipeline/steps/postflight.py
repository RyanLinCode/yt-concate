from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postfight')