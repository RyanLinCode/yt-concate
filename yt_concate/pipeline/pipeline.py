from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                # data 接收 調整完在傳給下一個
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happend', e)
                break