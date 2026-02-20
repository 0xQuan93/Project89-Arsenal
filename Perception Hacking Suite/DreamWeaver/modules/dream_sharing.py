import datetime

def record_dream(dream_content):
    """Records the dream content with a timestamp in a dream journal file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("dream_journal.txt", "a") as f:
        f.write(f"{timestamp}\n{dream_content}\n\n")

if __name__ == "__main__":
    # Example usage
    dream_content = "I was flying through the air, soaring above the clouds..."
    record_dream(dream_content)