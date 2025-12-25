from base_agent import BaseDeityAgent

class NatureAgent(BaseDeityAgent):
    def __init__(self):
        super().__init__(
            name="Sylvara",
            domain="Life/Seasons",
            system_prompt="",
            temperature=0.7
        )
