from .base_agent import BaseDeityAgent
from prompts.agent_prompts import DEATH_AGENT_PROMPT

class DeathAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Mortanis",
            domain="Endings/Rebirth",
            system_prompt=DEATH_AGENT_PROMPT,
            temperature=0.5
        )
