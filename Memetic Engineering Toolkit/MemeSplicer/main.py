from modules import image_manipulation, text_generation, virality_optimization
from typing import List, Tuple
import logging
import json
from pathlib import Path

def create_meme(
    image_path: str,
    keywords: List[str],
    font_path: str,
    font_size: int,
    text_color: Tuple[int, int, int],
    text_position: Tuple[int, int],
    output_path: str
) -> None:
    """Creates a meme by combining an image with a generated catchphrase.
    
    Args:
        image_path: Path to the source image
        keywords: List of keywords for catchphrase generation
        font_path: Path to the font file
        font_size: Size of the text
        text_color: RGB tuple for text color
        text_position: (x, y) position for text placement
        output_path: Path to save the output image
    
    Raises:
        FileNotFoundError: If image or font file not found
        ImageManipulationError: If image processing fails
    """
    try:
        image = image_manipulation.load_image(image_path)
        catchphrase = text_generation.generate_catchphrase(keywords)
        image_manipulation.add_text_to_image(image, catchphrase, font_path, font_size, text_color, text_position)
        image_manipulation.save_image(image, output_path)
    except Exception as e:
        logging.error(f"Failed to create meme: {str(e)}")
        raise

def get_network_data() -> dict:
    """Retrieves social network data for meme distribution"""
    try:
        network_file = Path("network_data.json")
        if not network_file.exists():
            return {"influencers": [], "connections": []}
        return json.loads(network_file.read_text())
    except Exception as e:
        logging.error(f"Failed to load network data: {e}")
        return {"influencers": [], "connections": []}

def distribute_meme(meme_path: str, influencers: List[dict]) -> None:
    """Distributes meme to network influencers"""
    try:
        for influencer in influencers:
            logging.info(f"Distributing meme to influencer: {influencer['id']}")
            # Implementation for actual distribution would go here
    except Exception as e:
        logging.error(f"Failed to distribute meme: {e}")
        raise

def main():
    try:
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