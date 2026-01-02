import json
from typing import List
from datetime import datetime

class LoreEntry:
    """
    Represents a single mythology story or lore entry in the database.
    
    Each LoreEntry contains a complete mythology story along with metadata
    about its creation, including which agents contributed to it and when
    it was created. This enables tracking and consistency checking.
    
    Attributes:
        title (str): The title or brief description of the mythology
        content (str): The full story content
        category (str): The type of mythology (e.g., "mythology", "origin_myth")
        contributors (List[str]): List of agent names that contributed to this story
        timestamp (str): ISO format timestamp of when the entry was created
    
    Args:
        title (str): Title or brief description of the story
        content (str): The complete mythology story text
        category (str): Category classification for the story
        contributors (List[str]): Names of agents that contributed to this story
    """
    
    def __init__(self, title: str, content: str, category: str, contributors: List[str]):
        self.title = title
        self.content = content 
        self.category = category
        self.contributors = contributors
        self.timestamp = datetime.now().isoformat()

class LoreDatabase:
    """
    Database for storing and managing mythology lore entries.
    
    The LoreDatabase maintains a collection of all mythology stories created
    by the agent collaboration system. It provides methods for adding new stories,
    retrieving existing lore for consistency checking, and persisting data to files.
    
    This class is crucial for maintaining consistency across multiple story
    creation sessions, as agents can reference previously created lore when
    generating new stories.
    
    Attributes:
        entries (List[LoreEntry]): List of all lore entries in the database
    
    """

    def __init__(self):
        self.entries = []

    def add_entry(self, title: str, content: str, category: str, contributors: List[str]):
        """
        Add a new lore entry to the database.
        
        Creates a new LoreEntry with the provided information and adds it to
        the database. The entry will automatically receive a timestamp when created.
        
        Args:
            title (str): Title or brief description of the mythology
            content (str): The complete story content
            category (str): Category classification (e.g., "mythology", "origin_myth")
            contributors (List[str]): List of agent names that contributed to this story
        
        Returns:
            LoreEntry: The newly created and added lore entry
        """
        entry = LoreEntry(title, content, category, contributors)
        self.entries.append(entry)
        return entry
    
    def get_all_lore(self) -> str:
        """
        Retrieve all stored lore as a formatted string.
        
        This method compiles all lore entries into a single formatted string
        that can be passed to agents as context. This ensures new stories
        are consistent with previously created mythology.
        
        Returns:
            str: Formatted string containing all lore entries, or "No existing lore."
                 if the database is empty. Each entry includes title, category, and content.
        
        Format:
            Title: [entry title]
            Category: [entry category]
            Content: [entry content]
            
            [next entry...]
        """
        if not self.entries:
            return "No existing lore."
        
        lore_text = ""
        for entry in self.entries:
            lore_text += f"Title: {entry.title}\n"
            lore_text += f"Category: {entry.category}\n"
            lore_text += f"Content: {entry.content}\n\n"
        return lore_text

    def save_to_file(self, filename: str):
        """
        Save all lore entries to a JSON file for persistence.
        
        Exports the entire lore database to a JSON file, preserving all
        metadata including titles, content, categories, contributors, and timestamps.
        This allows for backup, sharing, and loading of mythology collections.
        
        Args:
            filename (str): Path and filename for the JSON export file
        
        File Format:
            The JSON file contains an array of objects, each representing a lore entry:
            [
                {
                    "title": "The Shattered Moon",
                    "content": "Long ago...",
                    "category": "mythology",
                    "contributors": ["trickster", "weaver"],
                    "timestamp": "2024-01-01T12:00:00.000000"
                },
                ...
            ]
        
        Note:
            The file will be overwritten if it already exists.
        """
        data = []

        for entry in self.entries:
            data.append(
                {
                    "title": entry.title,
                    "content": entry.content,
                    "category": entry.category,
                    "contributors": entry.contributors,
                    "timestamp": entry.timestamp
                }
            )

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)