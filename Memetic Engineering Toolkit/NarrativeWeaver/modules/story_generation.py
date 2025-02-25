from typing import List

VALID_THEMES = {"awakening", "rebellion", "transcendence"}

def generate_story(theme: str, character_names: List[str], setting: str) -> str:
    """Generates a story based on theme, characters and setting
    
    Args:
        theme (str): The story theme ('awakening', 'rebellion', or 'transcendence')
        character_names (List[str]): List of character names (1-2 characters)
        setting (str): The story setting
        
    Returns:
        str: Generated story text
        
    Raises:
        ValueError: If inputs are empty or theme is invalid
    """
    if not theme or not character_names or not setting:
        raise ValueError("Theme, character names, and setting must not be empty")
    
    if not character_names[0].strip():
        raise ValueError("Primary character name must not be empty")
        
    if theme not in VALID_THEMES:
        raise ValueError(f"Theme must be one of: {', '.join(VALID_THEMES)}")
    
    story = f"In a {setting}, "
    
    themes = {
        "awakening": lambda: f"where {character_names[0]} begins to question the nature of reality. "
                           f"{'Meanwhile, ' + character_names[1] + ' works from the shadows to maintain the illusion.' if len(character_names) > 1 else ''}",
        "rebellion": lambda: f"where {character_names[0]} leads a resistance against the system. "
                           f"{'While ' + character_names[1] + ' attempts to maintain control through advanced technology.' if len(character_names) > 1 else ''}",
        "transcendence": lambda: f"where {character_names[0]} discovers the ability to manipulate the fabric of reality itself. "
                                f"{'But ' + character_names[1] + ' believes such power should remain hidden.' if len(character_names) > 1 else ''}"
    }
    
    story += themes.get(theme, lambda: "a story unfolds that challenges the very nature of existence.")()
    return story 