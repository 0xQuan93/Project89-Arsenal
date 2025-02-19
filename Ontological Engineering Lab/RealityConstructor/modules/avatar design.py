def create_avatar(name, appearance):
    """Creates an avatar with the specified name and appearance."""
    avatar = {
        "name": name,
        "appearance": appearance
    }
    return avatar

if __name__ == "__main__":
    # Example usage
    name = "Alice"
    appearance = {
        "hair": "black",
        "eyes": "blue",
        "height": 1.75
    }
    avatar = create_avatar(name, appearance)
    print(avatar)