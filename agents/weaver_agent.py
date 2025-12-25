from .base_agent import BaseDeityAgent

class WeaverAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Nyssara",
            domain="Synthesis/Harmony",
            system_prompt="",
            temperature=0.7
        )
