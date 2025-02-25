from modules import image_manipulation, text_generation

def create_meme(input_path, output_path, keywords, font_path="impact.ttf", font_size=50):
    try:
        # Load image
        image = image_manipulation.load_image(input_path)

        # Generate catchphrase
        catchphrase = text_generation.generate_catchphrase(keywords)

        # Add catchphrase to image
        # Calculate center position instead of hard-coding
        text_position = image_manipulation.calculate_text_position(image)
        image_manipulation.add_text_to_image(
            image, 
            catchphrase, 
            font_path, 
            font_size, 
            (255, 255, 255),  # white text
            text_position
        )

        # Save meme
        image_manipulation.save_image(image, output_path)
        return True
    except Exception as e:
        print(f"Error creating meme: {e}")
        return False

if __name__ == "__main__":
    keywords = ["Project 89", "awakening", "future"]
    create_meme("input.jpg", "output.jpg", keywords)