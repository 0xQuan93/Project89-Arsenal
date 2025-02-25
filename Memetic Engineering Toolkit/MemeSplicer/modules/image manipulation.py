from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """Loads an image from the specified path.
    
    Returns:
        PIL.Image or None: The loaded image or None if loading fails
    """
    try:
        image = Image.open(image_path)
        image.load()  # Validate image data
        return image
    except (FileNotFoundError, IOError) as e:
        print(f"Error loading image from {image_path}: {e}")
        return None

def add_text_to_image(image, text, font_path, font_size, text_color, text_position, align="left"):
    """Adds text to the image at the specified position.
    
    Args:
        image: PIL.Image object
        text: str to add to image
        font_path: path to font file
        font_size: integer font size
        text_color: RGB tuple
        text_position: (x, y) tuple
        align: text alignment ('left', 'center', 'right')
    """
    if not isinstance(image, Image.Image):
        raise ValueError("Invalid image object")
    
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError as e:
        print(f"Error loading font from {font_path}: {e}")
        return False
    
    # Get text size for alignment
    text_bbox = draw.textbbox(text_position, text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    
    # Adjust position based on alignment
    x, y = text_position
    if align == "center":
        x -= text_width // 2
    elif align == "right":
        x -= text_width
    
    draw.text((x, y), text, font=font, fill=text_color)
    return True

def save_image(image, output_path):
    """Saves the image to the specified path.
    
    Returns:
        bool: True if save successful, False otherwise
    """
    if not isinstance(image, Image.Image):
        print("Error: Invalid image object")
        return False
        
    try:
        image.save(output_path)
        return True
    except Exception as e:
        print(f"Error saving image to {output_path}: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    image_path = "input.jpg"
    text = "Wake Up"
    font_path = "impact.ttf"
    font_size = 50
    text_color = (255, 255, 255)  # White
    text_position = (10, 10)
    output_path = "output.jpg"

    image = load_image(image_path)
    if image:
        add_text_to_image(image, text, font_path, font_size, text_color, text_position)
        save_image(image, output_path)
        print(f"Meme created successfully: {output_path}")