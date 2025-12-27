from agents.death_agent import DeathAgent
from agents.wisdom_agent import WisdomAgent
from agents.nature_agent import NatureAgent
from agents.weaver_agent import WeaverAgent
from agents.warrior_agent import WarriorAgent
from memory.lore_database import LoreDatabase
from agents.trickster_agent import TricksterAgent
from orchestration.collaboration_patterns import CollaborativeSynthesis

class MythologyCoordinator:

    def __init__(self):
        # Initialize all agents
        self.agents = {
            "dealth": DeathAgent(),
            "wisdom": WisdomAgent(),
            "nature": NatureAgent(),
            "warrior": WarriorAgent(),
            "trickster": TricksterAgent()
        }

        self.weaver = WeaverAgent()
        self.lore_db = LoreDatabase()
        self.collaboration = CollaborativeSynthesis(self.agents, self.weaver)

    async def create_mythology(self, description: str):
        
        existing_lore = self.lore_db.get_all_lore()
        result = await self.collaboration.create_mythology(description, existing_lore)

        # save to database
        contributors = list(self.agents.keys()) + ['weaver']
        self.lore_db.add_entry(
            title=f"Mythology: {description[:50]}...",
            content=result['final_mythology'],
            category="Mythology",
            contributors=contributors
        )

        return result
    
    def get_all_lore(self):
        return self.lore_db.get_all_lore()
    
    def save_lore(self, filename: str):
        self.lore_db.save_to_file(filename)

        
