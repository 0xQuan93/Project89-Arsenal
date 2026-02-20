def generate_nlp_script(target_behavior):
    """Generates an NLP script to influence the target behavior."""
    script = f"""
    1. Establish rapport.
    2. Identify the target behavior: {target_behavior}
    3. Elicit the target's current state.
    4. Anchor the target's desired state.
    5. Link the desired state to the target behavior.
    6. Test the new association.
    """
    return script

if __name__ == "__main__":
    # Example usage
    target_behavior = "questioning reality"
    nlp_script = generate_nlp_script(target_behavior)
    print(nlp_script)