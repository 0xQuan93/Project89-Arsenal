import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import os
from utils import create_meme, distribute_meme, get_network_data

class MemeSplicerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemeSplicer Drag and Drop")
        self.root.geometry("600x600")

        self.image_path = None

        # Image selection
        self.label = tk.Label(root, text="Drag and drop an image file here", width=60, height=10, bg="lightgray")
        self.label.pack(pady=10)
        self.label.bind("<Button-1>", self.browse_files)

        # Keywords entry
        tk.Label(root, text="Keywords (comma-separated):").pack()
        self.keywords_entry = tk.Entry(root, width=50)
        self.keywords_entry.pack(pady=5)

        # Font path entry
        tk.Label(root, text="Font Path:").pack()
        self.font_path_entry = tk.Entry(root, width=50)
        self.font_path_entry.insert(0, "impact.ttf")
        self.font_path_entry.pack(pady=5)

        # Font size entry
        tk.Label(root, text="Font Size:").pack()
        self.font_size_entry = tk.Entry(root, width=10)
        self.font_size_entry.insert(0, "50")
        self.font_size_entry.pack(pady=5)

        # Text color selection
        tk.Label(root, text="Text Color:").pack()
        self.text_color_button = tk.Button(root, text="Select Color", command=self.choose_color)
        self.text_color_button.pack(pady=5)
        self.text_color = (255, 255, 255)  # Default white

        # Text position entry
        tk.Label(root, text="Text Position (x, y):").pack()
        self.text_position_entry = tk.Entry(root, width=20)
        self.text_position_entry.insert(0, "10, 10")
        self.text_position_entry.pack(pady=5)

        # Output path entry
        tk.Label(root, text="Output Path:").pack()
        self.output_path_entry = tk.Entry(root, width=50)
        self.output_path_entry.insert(0, "output.jpg")
        self.output_path_entry.pack(pady=5)

        # Create meme button
        self.create_button = tk.Button(root, text="Create Meme", command=self.create_meme)
        self.create_button.pack(pady=20)

        # Distribute meme button
        self.distribute_button = tk.Button(root, text="Distribute Meme", command=self.distribute_meme)
        self.distribute_button.pack(pady=10)

    def browse_files(self, event):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.label.config(text=os.path.basename(self.image_path))

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose text color")
        if color_code:
            self.text_color = tuple(map(int, color_code[0]))

    def create_meme(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image file.")
            return

        try:
            # Define configuration for meme creation
            config = {
                "image_path": self.image_path,
                "keywords": self.keywords_entry.get().split(","),
                "font_path": self.font_path_entry.get(),
                "font_size": int(self.font_size_entry.get()),
                "text_color": self.text_color,
                "text_position": tuple(map(int, self.text_position_entry.get().split(","))),
                "output_path": self.output_path_entry.get()
            }

            # Create meme
            create_meme(**config)

            # Display the output image
            self.display_output_image(config["output_path"])

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def distribute_meme(self):
        try:
            network_data = get_network_data()
            top_influencers = network_data.get("influencers", [])
            distribute_meme(self.output_path_entry.get(), top_influencers)
            messagebox.showinfo("Success", "Meme distributed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_output_image(self, output_path):
        img = Image.open(output_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)

        if hasattr(self, 'output_label'):
            self.output_label.config(image=img)
            self.output_label.image = img
        else:
            self.output_label = tk.Label(self.root, image=img)
            self.output_label.image = img
            self.output_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeSplicerApp(root)
    root.mainloop() 