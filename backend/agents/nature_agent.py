from .base_agent import BaseDeityAgent
from prompts.agent_prompts import NATURE_AGENT_PROMPT

class NatureAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Sylvara",
            domain="Life/Seasons",
            system_prompt=NATURE_AGENT_PROMPT,
            temperature=0.7
        )
