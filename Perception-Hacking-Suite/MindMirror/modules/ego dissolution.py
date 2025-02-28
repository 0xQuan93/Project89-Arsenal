def challenge_beliefs(belief_system):
    """Challenges the user's beliefs to promote ego dissolution."""
    questions = [
        "Is this belief really true?",
        "How does this belief serve you?",
        "What would happen if you let go of this belief?",
        "Who would you be without this belief?"
    ]
    for belief in belief_system:
        print(f"Belief: {belief}")
        for question in questions:
            print(f"  - {question}")
        print("\n")

if __name__ == "__main__":
    # Example usage
    belief_system = {
        "belief1": "I am separate from others.",
        "belief2": "I am limited by my past.",
        "belief3": "I am not good enough."
    }
    challenge_beliefs(belief_system)