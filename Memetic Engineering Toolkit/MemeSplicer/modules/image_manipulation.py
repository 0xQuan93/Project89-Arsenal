from PIL import Image, ImageDraw, ImageFont

def load_image(image_path):
    """Loads an image from the specified path."""
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

def add_text_to_image(image, text, font_path, font_size, text_color, text_position):
    """Adds text to the image at the specified position."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(text_position, text, font=font, fill=text_color)

def save_image(image, output_path):
    """Saves the image to the specified path."""
    try:
        image.save(output_path)
    except Exception as e:
        print(f"Error saving image: {e}")

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