from .base_agent import BaseDeityAgent

class DeathAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Mortanis",
            domain="Endings/Rebirth",
            system_prompt="",
            temperature=0.5
        )
