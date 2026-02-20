from modules import story_generation, character_development, plot_twist_generator

def weave_narrative(theme, character_names, archetypes, setting):
    """Weaves a narrative with characters, plot twists, and a resolution."""
    characters = [character_development.create_character(name, archetype) for name, archetype in zip(character_names, archetypes)]
    story = story_generation.generate_story(theme, [character["name"] for character in characters], setting)
    twist = plot_twist_generator.generate_plot_twist(story)
    story += f"\n{twist}"
    return story

def main():
    theme = "awakening"
    character_names = ["Alice", "Bob"]
    archetypes = ["hero", "villain"]
    setting = "simulated reality"
    narrative = weave_narrative(theme, character_names, archetypes, setting)
    print(narrative)

if __name__ == "__main__":
    main()