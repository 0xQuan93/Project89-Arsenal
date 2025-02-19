import random

def generate_contradictory_statements(belief_system):
    """Generates contradictory statements that challenge the belief system."""
    statements = [
        "The world is both flat and round.",
        "You are both awake and dreaming.",
        "Reality is both real and simulated."
    ]
    return random.choice(statements)

if __name__ == "__main__":
    # Example usage
    belief_system = {
        "belief1": "The world is flat.",
        "belief2": "The Earth is the center of the universe.",
        "belief3": "Humans are inherently evil."
    }
    contradictory_statement = generate_contradictory_statements(belief_system)
    print(contradictory_statement)