from modules import story_generation, character_development, plot_twist_generator

# Create characters
alice = character_development.create_character("Alice", "hero")
bob = character_development.create_character("Bob", "villain")

# Generate story
story = story_generation.generate_story("awakening", [alice["name"], bob["name"]], "simulated reality")

# Add plot twist
twist = plot_twist_generator.generate_plot_twist(story)
story += f"\n{twist}"

print(story)