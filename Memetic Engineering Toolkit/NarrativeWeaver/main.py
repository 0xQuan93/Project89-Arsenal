from typing import List, Dict
from modules import story_generation, character_development, plot_twist_generator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def weave_narrative(theme: str, character_names: List[str], archetypes: List[str], setting: str) -> str:
    """Weaves a narrative with characters, plot twists, and a resolution.
    
    Args:
        theme: The central theme of the story
        character_names: List of character names
        archetypes: List of character archetypes
        setting: The story's setting
    
    Returns:
        str: The complete narrative including plot twist
        
    Raises:
        ValueError: If character_names and archetypes lists have different lengths
    """
    if len(character_names) != len(archetypes):
        raise ValueError("Number of character names must match number of archetypes")
        
    try:
        characters = [
            character_development.create_character(name, archetype) 
            for name, archetype in zip(character_names, archetypes)
        ]
        story = story_generation.generate_story(theme, [character["name"] for character in characters], setting)
        twist = plot_twist_generator.generate_plot_twist(story)
        return f"{story}\n{twist}"
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        raise
    except KeyError as ke:
        logging.error(f"KeyError: {str(ke)}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise RuntimeError(f"Failed to generate narrative: {str(e)}")

def main():
    theme = "awakening"
    character_names = ["Alice", "Bob"]
    archetypes = ["hero", "villain"]
    setting = "simulated reality"
    narrative = weave_narrative(theme, character_names, archetypes, setting)
    print(narrative)

if __name__ == "__main__":
    main()