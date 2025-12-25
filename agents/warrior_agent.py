from base_agent import BaseDeityAgent

class WarriorAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Valdris",
            domain="Conflict/Honor",
            system_prompt="",
            temperature=0.6
        )
