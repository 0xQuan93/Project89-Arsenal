import tkinter as tk
from tkinter import simpledialog

def incubate_dream():
    """Prompts the user for a dream topic and provides suggestions for incubation."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get desired dream topic
    topic = simpledialog.askstring("Input", "What do you want to dream about?", parent=root)

    if topic:
        suggestions = f"To incubate a dream about {topic}, try these before sleep:\n\n- Visualize {topic} vividly.\n- Repeat affirmations related to {topic}.\n- Draw or write about {topic}.\n- Meditate on {topic}.\n- Fall asleep while thinking about {topic}."

        # Display the suggestions in a messagebox
        tk.messagebox.showinfo("Dream Incubation", suggestions)

if __name__ == "__main__":
    incubate_dream()