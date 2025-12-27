from .base_agent import BaseDeityAgent
from prompts.agent_prompts import WISDOM_AGENT_PROMPT

class WisdomAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Aetherion",
            domain="Knowledge/Magic",
            system_prompt=WISDOM_AGENT_PROMPT,
            temperature=0.7
        )
