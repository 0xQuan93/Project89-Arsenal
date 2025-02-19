from modules import image_manipulation, text_generation

# Load image
image = image_manipulation.load_image("input.jpg")

# Generate catchphrase
keywords = ["Project 89", "awakening", "future"]
catchphrase = text_generation.generate_catchphrase(keywords)

# Add catchphrase to image
image_manipulation.add_text_to_image(image, catchphrase, "impact.ttf", 50, (255, 255, 255), (10, 10))

# Save meme
image_manipulation.save_image(image, "output.jpg")