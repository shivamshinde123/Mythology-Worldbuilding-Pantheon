
import asyncio

class CollaborativeSynthesis:
    """
    Orchestrates collaborative mythology creation using multiple AI agents.
    
    This class implements the Collaborative Synthesis pattern, where multiple
    deity agents work together in a structured sequence to create rich, coherent
    mythologies. The process involves problem analysis, sequential agent
    contributions, and final synthesis.
    
    The collaboration follows a three-step process:
    1. Problem Definition: Creation Weaver analyzes the request
    2. Agent Collaboration: Each deity agent contributes their perspective
    3. Final Synthesis: Creation Weaver combines all contributions
    
    Attributes:
        agents (dict): Dictionary of deity agents {name: agent_instance}
        weaver (BaseDeityAgent): The Creation Weaver agent for synthesis
    
    Args:
        agents (dict): Dictionary mapping agent names to agent instances
        weaver_agent (BaseDeityAgent): The Creation Weaver agent instance

    """

    def __init__(self, agents, weaver_agent):
        self.agents = agents
        self.weaver = weaver_agent

    async def create_mythology(self, task: str, existing_lore: str = ""):
        """
        Create a collaborative mythology using all deity agents.
        
        This is the main method that orchestrates the entire collaborative process.
        It coordinates multiple AI agents to create a rich, coherent mythology
        that incorporates each agent's unique perspective and domain expertise.
        
        The process follows three phases:
        
        Phase 1 - Problem Definition:
            The Creation Weaver analyzes the request and identifies what elements
            are needed for a complete mythology.
        
        Phase 2 - Sequential Agent Collaboration:
            Each deity agent contributes their perspective in sequence, with later
            agents able to see and build upon earlier agents' contributions.
        
        Phase 3 - Final Synthesis:
            The Creation Weaver combines all agent contributions into a single,
            coherent narrative that honors all perspectives.
        
        Args:
            task (str): The mythology creation request (e.g., "Create a dragon origin story")
            existing_lore (str, optional): Previously created lore for consistency.
                                         Defaults to empty string.
        
        Returns:
            dict: Dictionary containing the complete collaboration results:
                - problem_definition (str): Weaver's analysis of what's needed
                - agent_responses (List[str]): All individual agent contributions
                - final_mythology (str): The synthesized final story
        
        Note:
            This method uses sequential collaboration where each agent can see
            previous agents' responses, leading to more integrated stories.
        """
        # Step 1: Weaver defines the problem
        problem = await self.weaver.ainvoke(f"Briefly analyze what aspects need to be covered for: {task}. Don't write the story, just identify what elements are needed.", {"existing_lore": existing_lore})

        # Step 2: All agents work on it together
        agent_responses = []
        context = {"existing_lore": existing_lore, "problem": problem}

        for agent_name, agent in self.agents.items():
            response = await agent.ainvoke(task, context)
            agent_responses.append(f"{agent_name}: {response}")
            context["previous_responses"] = "\n\n".join(agent_responses)

        # Step 3: Weaver creates final version
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