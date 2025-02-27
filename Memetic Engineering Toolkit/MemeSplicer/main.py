from modules import image_manipulation, text_generation, virality_optimization
from typing import List, Tuple
import logging
import json
from pathlib import Path
from gui import MemeSplicerApp
import tkinter as tk
from utils import create_meme, distribute_meme, get_network_data

def main():
    try:
        # Initialize and run the GUI
        root = tk.Tk()
        app = MemeSplicerApp(root)
        root.mainloop()

        # Get network data
        network_data = get_network_data()

        # Analyze network
        top_influencers = virality_optimization.analyze_network(network_data)

        # Load configuration (consider moving to config file)
        config = {
            "image_path": "input.jpg",
            "keywords": ["Project 89", "awakening", "future"],
            "font_path": "impact.ttf",
            "font_size": 50,
            "text_color": (255, 255, 255),
            "text_position": (10, 10),
            "output_path": "output.jpg"
        }

        # Create meme
        create_meme(**config)

        # Distribute meme to top influencers
        distribute_meme(config["output_path"], top_influencers)

    except Exception as e:
        logging.error(f"Main execution failed: {str(e)}")
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()