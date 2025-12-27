
import asyncio

class CollaborativeSynthesis:

    def __init__(self, agents, weaver_agent):
        self.agents = agents
        self.weaver = weaver_agent

    async def create_mythology(self, task: str, existing_lore: str = ""):
        # step 1: weaver defines the problem
        problem = await self.weaver.ainvoke(f"Briefly analyze what aspects need to be covered for: {task}. Don't write the story, just identify what elements are needed.", {"existing_lore": existing_lore})

        # step 2: all agents work on it together
        agent_responses = []
        context = {"existing_lore": existing_lore, "problem": problem}

        for agent_name, agent in self.agents.items():
            response = await agent.ainvoke(task, context)
            agent_responses.append(f"{agent_name}: {response}")
            context["previous_responses"] = "\n\n".join(agent_responses)

        # step 3: weaver creates final version
        final_context = {
            "existing_lore": existing_lore,
            "original_request": task,
            "agent_responses": "\n\n".join(agent_responses)
        }

        final_mythology = await self.weaver.ainvoke(f"Write a single, clean story for: {task}. Use the best ideas from all agents but write it as one flowing narrative without any meta-commentary, analysis, or section headers. Just tell the story.", final_context)

        return {
            "problem_definition": problem,
            "agent_responses": agent_responses,
            "final_mythology": final_mythology
        }