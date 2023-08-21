from step import CreateOrderStep, UpdateOrderStatusStep, GetMenuStep, PublishErrorStep

class Workflow:
    def __init__(self):
        self.steps = [
            CreateOrderStep(),
            UpdateOrderStatusStep(),
            GetMenuStep(),
            PublishErrorStep()
        ]

    def execute(self, data):
        for step in self.steps:
            data = step.execute(data)
