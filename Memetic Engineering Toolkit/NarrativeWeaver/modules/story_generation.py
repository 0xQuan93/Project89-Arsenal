from typing import List

def generate_story(theme: str, character_names: List[str], setting: str) -> str:
    """Generates a story based on theme, characters and setting"""
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