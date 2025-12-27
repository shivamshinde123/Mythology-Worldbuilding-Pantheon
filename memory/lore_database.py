
import json
from typing import List
from datetime import datetime

class LoreEntry:
    
    def __init__(self, title: str, content: str, category: str, contributors: List[str]):
        self.title = title
        self.content = content 
        self.category = category
        self.contributors = contributors
        self.timestamp = datetime.now().isoformat()

class LoreDatabase:

    def __init__(self):
        self.entries = []

    def add_entry(self, title: str, content: str, category: str, contributors: List[str]):
        entry = LoreEntry(title, content, category, contributors)
        self.entries.append(entry)
        return entry
    
    def get_all_lore(self) -> str:

        if not self.entries:
            return "No existing lore."
        
        lore_text = ""
        for entry in self.entries:
            lore_text += f"Title: {entry.title}\n"
            lore_text += f"Category: {entry.category}\n"
            lore_text += f"Content: {entry.content}\n"
        return lore_text

    def save_to_file(self, filename: str):
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