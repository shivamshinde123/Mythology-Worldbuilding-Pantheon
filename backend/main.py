import os
import uvicorn
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from orchestration.coordinator import MythologyCoordinator
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

async def extract_story(raw_output: str) -> str:
    """
    Extract clean story content from raw agent output using LLM.
    
    This function uses a separate LLM call to clean up the mythology output by removing
    meta-commentary, instructions, quality checks, and other non-narrative content,
    leaving only the pure story.
    
    Args:
        raw_output (str): The raw output from the Creation Weaver agent, which may
                         contain meta-commentary and formatting artifacts.
    
    Returns:
        str: Clean narrative content with all meta-commentary removed.
    """
    # Use LLM to extract just the story from the raw output
    llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

    messages = [
        SystemMessage(content="Extract only the story from the given text. Remove all instructions, templates, quality checks, and meta-commentary. Return only the pure narrative."),
        HumanMessage(content=raw_output)
    ]

    response = await llm.ainvoke(messages)
    return response.content

async def main():
    """
    Main function demonstrating the mythology creation system.
    
    This function initializes the MythologyCoordinator, creates a sample mythology
    about the moon shattering, extracts the clean story content, and prints it.
    Serves as an example of how to use the system.
    
    The function demonstrates:
    - Initializing the coordinator
    - Making a mythology creation request
    - Extracting clean story content
    - Displaying the result
    """
    coordinator = MythologyCoordinator()
    result = await coordinator.create_mythology("Create a story about when the moon was shattered. It should have beginning, and proper ending.")
    
    # Extract clean story using LLM
    clean_story = await extract_story(result['final_mythology'])
    print(clean_story)

if __name__ == "__main__":
    uvicorn.run("api.routes:app", host="127.0.0.1", port=8000)


    