from agent.memory import Memory
from agent.reasoning import make_decision

class Agent:
    def __init__(self):
        self.memory = Memory()

    def process(self, input_item):
        self.memory.remember(input_item)
        decision = make_decision(self.memory.recall())
        return decision
