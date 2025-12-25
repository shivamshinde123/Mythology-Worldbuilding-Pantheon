from .base_agent import BaseDeityAgent

class WisdomAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Aetherion",
            domain="Knowledge/Magic",
            system_prompt="",
            temperature=0.7
        )
