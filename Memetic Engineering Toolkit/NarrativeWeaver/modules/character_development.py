from typing import Dict, TypedDict, List

class CharacterData(TypedDict):
    name: str
    archetype: str
    traits: List[str]
    motivation: str

def create_character(name: str, archetype: str) -> CharacterData:
    """Creates a character with given name and archetype
    
    Args:
        name: Character's name
        archetype: Character's archetype (e.g., 'hero', 'villain')
        
    Returns:
        CharacterData containing character information
    """
    traits = {
        "hero": ["brave", "questioning", "determined"],
        "villain": ["manipulative", "controlling", "powerful"],
        "mentor": ["wise", "guiding", "experienced"],
        "sidekick": ["loyal", "supportive", "resourceful"]
    }
    
    motivations = {
        "hero": "to bring positive change to the system",
        "villain": "to reshape the system through dominance",
        "mentor": "to guide others toward understanding",
        "sidekick": "to support and learn from others"
    }
    
    return {
        "name": name,
        "archetype": archetype,
        "traits": traits.get(archetype, ["mysterious", "undefined"]),
        "motivation": motivations.get(archetype, "to find their place in the system")
    } 