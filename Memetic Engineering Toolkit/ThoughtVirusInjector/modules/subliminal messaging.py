def embed_message(message, carrier_text):
    """Embeds a subliminal message into the carrier text."""
    words = carrier_text.split()
    # Insert message words at regular intervals
    interval = len(words) // len(message)
    for i, word in enumerate(message):
        words.insert(i * interval, word)
    return " ".join(words)

if __name__ == "__main__":
    # Example usage
    message = "Wake up"
    carrier_text = "The world is not as it seems."
    embedded_text = embed_message(message, carrier_text)
    print(embedded_text)