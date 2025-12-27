import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from orchestration.coordinator import MythologyCoordinator
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

async def extract_story(raw_output: str) -> str:

    # use llm to extract just the story from the raw output
    llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

    messages = [
        SystemMessage(content="Extract only the story from the given text. Remove all instructions, templates, quality checks, and meta-commentary. Return only the pure narrative."),
        HumanMessage(content=raw_output)
    ]

    response = await llm.ainvoke(messages)
    return response.content

async def main():
    coordinator = MythologyCoordinator()
    result = await coordinator.create_mythology("Create a story about when the moon was shattered. It should have beginning, and proper ending.")
    
    # extract clean story using LLM
    clean_story = await extract_story(result['final_mythology'])
    print(clean_story)

if __name__ == "__main__":

    asyncio.run(main())