
import asyncio
from typing import Dict, Any, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class BaseDeityAgent:

    def __init__(self, name: str, domain: str, system_prompt: str, temperature: float = 0.7):
        self.name = name
        self.domain = domain
        self.system_prompt = system_prompt
        self.llm = ChatOpenAI(
            model = "gpt-4o",
            temperature = temperature
        )

    def invoke(self, task: str, context: Dict[str, Any] = None) -> str:

        "synchronous invoke"

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.format_input(task, context))
        ]

        response = self.llm.invoke(messages)
        return response.content
    
    async def ainvoke(self, task: str, context: Dict[str, Any] = None) -> str:

        "asynchronous invoke"

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=self.format_input(task, context))
        ]

        response = await self.llm.ainvoke(messages)
        return response.content


    def format_input(self, task: str, context: dict[str, Any] = None) -> str:

        "format inputs with context"

        formatted = f"Task: {task}\n\n"

        if context:
            if context.get("existing_lore"):
                formatted += f"Existing Lore: \n {context['existing_lore']}\n\n"
            if context.get("previous_responses"):
                formatted += f"Previous Agent Responses: \n {context['previous_responses']}\n\n"

    
        return formatted
    
    def get_info(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "domain": self.domain,
            "temperature": str(self.llm.temperature)
        }
    
    