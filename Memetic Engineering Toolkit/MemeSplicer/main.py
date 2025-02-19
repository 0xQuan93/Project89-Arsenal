from modules import image_manipulation, text_generation, virality_optimization

def create_meme(image_path, keywords, font_path, font_size, text_color, text_position, output_path):
    """Creates a meme by combining an image with a generated catchphrase."""
    image = image_manipulation.load_image(image_path)
    catchphrase = text_generation.generate_catchphrase(keywords)
    image_manipulation.add_text_to_image(image, catchphrase, font_path, font_size, text_color, text_position)
    image_manipulation.save_image(image, output_path)

def main():
    # Get network data
    network_data = get_network_data()

    # Analyze network
    top_influencers = virality_optimization.analyze_network(network_data)

    # Create meme
    image_path = "input.jpg"
    keywords = ["Project 89", "awakening", "future"]
    font_path = "impact.ttf"
    font_size = 50
    text_color = (255, 255, 255)
    text_position = (10, 10)
    output_path = "output.jpg"
    create_meme(image_path, keywords, font_path, font_size, text_color, text_position, output_path)

    # Distribute meme to top influencers
    distribute_meme(output_path, top_influencers)

if __name__ == "__main__":
    main()