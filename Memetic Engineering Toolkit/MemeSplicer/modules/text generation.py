import random

def generate_catchphrase(keywords):
    """Generates a catchphrase based on the provided keywords.
    
    Args:
        keywords (list): List of strings to use in the catchphrase.
                        Must contain exactly 3 elements.
    
    Returns:
        str: Generated catchphrase
        
    Raises:
        ValueError: If keywords list doesn't contain exactly 3 elements
    """
    if not isinstance(keywords, list) or len(keywords) != 3:
        raise ValueError("Keywords must be a list containing exactly 3 elements")
        
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