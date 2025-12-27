
from .base_agent import BaseDeityAgent
from prompts.agent_prompts import TRICKSTER_AGENT_PROMPT

class TricksterAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name= "Kethix",
            domain="Chaos/Change",
            system_prompt=TRICKSTER_AGENT_PROMPT,
            temperature=0.9
        )