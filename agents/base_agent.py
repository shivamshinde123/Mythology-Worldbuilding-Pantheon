
import asyncio
from typing import Dict, Any, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class BaseDeityAgent:
    """
    Base class for all deity agents in the mythology creation system.
    
    This class provides the foundational functionality for AI agents that represent
    different deity archetypes. Each deity agent has a unique personality, domain,
    and system prompt that defines their behavior and contributions to mythology creation.
    
    The class handles LangChain integration, context management, and provides both
    synchronous and asynchronous methods for invoking the underlying language model.
    
    Attributes:
        name (str): The deity's name (e.g., "Kethix", "Valdris")
        domain (str): The deity's domain of influence (e.g., "Chaos/Change", "Conflict/Honor")
        system_prompt (str): The detailed personality and behavior prompt for the agent
        llm (ChatOpenAI): The language model instance configured for this agent
    
    Args:
        name (str): The name of the deity agent
        domain (str): The domain or sphere of influence for this deity
        system_prompt (str): The system prompt that defines the agent's personality
        temperature (float, optional): The creativity/randomness setting for the LLM.
                                     Defaults to 0.7. Range: 0.0 (deterministic) to 1.0 (creative)

    """

    def __init__(self, name: str, domain: str, system_prompt: str, temperature: float = 0.7):
        self.name = name
        self.domain = domain
        self.system_prompt = system_prompt
        self.llm = ChatOpenAI(
            model = "gpt-4o",
            temperature = temperature
        )

    def invoke(self, task: str, context: Dict[str, Any] = None) -> str:
        """
        Synchronously invoke the deity agent to respond to a task.
        
        This method sends a task to the language model along with any provided context
        and returns the agent's response. The response reflects the agent's unique
        personality and domain expertise.
        
        Args:
            task (str): The mythology creation task or question for the agent
            context (Dict[str, Any], optional): Additional context including existing lore
                                              and previous agent responses. Defaults to None.
        
        Returns:
            str: The agent's response to the task, formatted according to their personality
        
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.format_input(task, context))
        ]

        response = self.llm.invoke(messages)
        return response.content
    
    async def ainvoke(self, task: str, context: Dict[str, Any] = None) -> str:
        """
        Asynchronously invoke the deity agent to respond to a task.
        
        This is the async version of invoke(), allowing for concurrent execution
        of multiple agents. Used in the collaborative synthesis process where
        multiple agents work together.
        
        Args:
            task (str): The mythology creation task or question for the agent
            context (Dict[str, Any], optional): Additional context including existing lore,
                                              previous agent responses, and problem definition.
                                              Defaults to None.
        
        Returns:
            str: The agent's response to the task, reflecting their unique perspective
        
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.format_input(task, context))
        ]

        response = await self.llm.ainvoke(messages)
        return response.content


    def format_input(self, task: str, context: dict[str, Any] = None) -> str:
        """
        Format the input prompt for the language model with task and context.
        
        This method constructs the final prompt that will be sent to the language model
        by combining the task with any available context information such as existing
        lore and previous agent responses.
        
        Args:
            task (str): The main task or question for the agent
            context (dict[str, Any], optional): Dictionary containing contextual information.
                                              May include 'existing_lore' and 'previous_responses'.
                                              Defaults to None.
        
        Returns:
            str: Formatted prompt string ready to be sent to the language model
        
        Context Keys:
            - existing_lore: Previously created mythology stories for consistency
            - previous_responses: Responses from other agents in the current session
            - problem: Problem definition from the Creation Weaver
        
        """
        formatted = f"Task: {task}\n\n"

        if context:
            if context.get("existing_lore"):
                formatted += f"Existing Lore: \n {context['existing_lore']}\n\n"
            if context.get("previous_responses"):
                formatted += f"Previous Agent Responses: \n {context['previous_responses']}\n\n"

        return formatted
    
    def get_info(self) -> Dict[str, str]:
        """
        Get basic information about this deity agent.
        
        Returns a dictionary containing the agent's name, domain, and temperature setting.
        Useful for debugging, logging, or displaying agent information in user interfaces.
        
        Returns:
            Dict[str, str]: Dictionary with agent information
                - name: The deity's name
                - domain: The deity's domain of influence  
                - temperature: The LLM temperature setting as a string
        """
        return {
            "name": self.name,
            "domain": self.domain,
            "temperature": str(self.llm.temperature)
        }
    
    