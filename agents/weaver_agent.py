from .base_agent import BaseDeityAgent
from prompts.agent_prompts import CREATION_WEAVER_PROMPT

class WeaverAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Nyssara",
            domain="Synthesis/Harmony",
            system_prompt=CREATION_WEAVER_PROMPT,
            temperature=0.7
        )
