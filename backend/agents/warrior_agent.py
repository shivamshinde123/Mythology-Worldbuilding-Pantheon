from .base_agent import BaseDeityAgent
from prompts.agent_prompts import WARRIOR_AGENT_PROMPT

class WarriorAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Valdris",
            domain="Conflict/Honor",
            system_prompt=WARRIOR_AGENT_PROMPT,
            temperature=0.6
        )
