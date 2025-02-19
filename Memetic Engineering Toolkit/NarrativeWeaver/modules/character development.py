import random

def create_character(name, archetype):
    """Creates a character with the given name and archetype."""
    character = {
        "name": name,
        "archetype": archetype,
        "traits":,
        "motivations":
    }
    # Assign traits based on archetype
    if archetype == "hero":
        character["traits"] = ["brave", "determined", "selfless"]
        character["motivations"] = ["save the world", "defeat evil", "protect the innocent"]
    elif archetype == "villain":
        character["traits"] = ["cruel", "ambitious", "power-hungry"]
        character["motivations"] = ["rule the world", "destroy the hero", "gain ultimate power"]
    else:
        character["traits"] = ["curious", "intelligent", "open-minded"]
        character["motivations"] = ["seek knowledge", "discover the truth", "explore the unknown"]
    return character

if __name__ == "__main__":
    # Example usage
    name = "Alice"
    archetype = "hero"
    character = create_character(name, archetype)
    print(character)