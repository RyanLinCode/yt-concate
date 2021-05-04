from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                print('data:', data)
                # data 接收 調整完在傳給下一個
                data = step.process(data, inputs, utils)
                print('2data:', data)
            except StepException as e:
                print('Exception happend', e)
                break
