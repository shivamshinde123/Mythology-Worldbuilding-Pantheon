
from base_agent import BaseDeityAgent

class TricksterAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name= "kethix",
            domain="Chaos/Change",
            system_prompt="",
            temperature=0.9
        )