import tkinter as tk
from tkinter import simpledialog

def show_reflection():
    """Displays a mirror-like interface for self-reflection."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Get user's name
    name = simpledialog.askstring("Input", "What is your name?", parent=root)

    if name:
        reflection_text = f"Hello, {name}. Look closely. What do you see?\n\nBeyond the surface, beyond the labels, beyond the roles you play...\n\nWho are you, really?\n\nWhat is your purpose?\n\nWhat is your potential?"

        # Display the reflection text in a messagebox
        tk.messagebox.showinfo("Reflection", reflection_text)

if __name__ == "__main__":
    show_reflection()