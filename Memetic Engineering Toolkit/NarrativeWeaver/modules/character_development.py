from typing import Dict

def create_character(name: str, archetype: str) -> Dict:
    """Creates a character with given name and archetype"""
    traits = {
        "hero": ["brave", "questioning", "determined"],
        "villain": ["manipulative", "controlling", "powerful"]
    }
    
    return {
        "name": name,
        "archetype": archetype,
        "traits": traits.get(archetype, []),
        "motivation": f"To {'save' if archetype == 'hero' else 'control'} the system"
    } 