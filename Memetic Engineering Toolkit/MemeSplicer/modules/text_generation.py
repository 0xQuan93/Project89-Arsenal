import random

def generate_catchphrase(keywords):
    """Generates a catchphrase based on the provided keywords."""
    templates = [
        "{}: The {} is now.",
        "{}: {} the {}.",
        "{}: {} your {}.",
        "{}: The {} of {}.",
        "{}: {} is the new {}."
    ]
    template = random.choice(templates)
    return template.format(*keywords)

if __name__ == "__main__":
    # Example usage
    keywords = ["Project 89", "awakening", "future"]
    catchphrase = generate_catchphrase(keywords)
    print(catchphrase)