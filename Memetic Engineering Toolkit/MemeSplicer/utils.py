from modules import image_manipulation, text_generation
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
    except FileNotFoundError:
        logging.error(f"Image file not found: {image_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading image: {str(e)}")
        raise

    try:
        catchphrase = text_generation.generate_catchphrase(keywords)
    except Exception as e:
        logging.error(f"Error generating catchphrase: {str(e)}")
        raise

    try:
        image_manipulation.add_text_to_image(image, catchphrase, font_path, font_size, text_color, text_position)
    except FileNotFoundError:
        logging.error(f"Font file not found: {font_path}")
        raise
    except Exception as e:
        logging.error(f"Error adding text to image: {str(e)}")
        raise

    try:
        image_manipulation.save_image(image, output_path)
    except Exception as e:
        logging.error(f"Error saving image: {str(e)}")
        raise


def get_network_data() -> dict:
    """Retrieves social network data for meme distribution"""
    try:
        network_file = Path("network_data.json")
        if not network_file.exists():
            logging.warning("Network data file not found, using default empty data.")
            return {"influencers": [], "connections": []}
        return json.loads(network_file.read_text())
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from network data file: {e}")
        return {"influencers": [], "connections": []}
    except Exception as e:
        logging.error(f"Failed to load network data: {e}")
        return {"influencers": [], "connections": []}


def distribute_meme(meme_path: str, influencers: List[dict]) -> None:
    """Distributes meme to network influencers"""
    try:
        for influencer in influencers:
            logging.info(f"Distributing meme to influencer: {influencer['id']}")
            # Implementation for actual distribution would go here
    except KeyError as e:
        logging.error(f"Influencer data missing key: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to distribute meme: {e}")
        raise 