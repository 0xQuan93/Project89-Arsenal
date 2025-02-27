# MemeSplicer

MemeSplicer is a component of the Memetic Engineering Toolkit designed to create and distribute memes using advanced image manipulation, text generation, and virality optimization techniques.

## Features

- **Image Manipulation**: Load and modify images to create memes.
- **Text Generation**: Generate catchy phrases based on provided keywords.
- **Virality Optimization**: Analyze social networks to optimize meme distribution.

## Requirements

- Python 3.6 or higher
- Required Python packages (install using `requirements.txt` if available)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Memetic\ Engineering\ Toolkit/MemeSplicer
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Meme Settings**: Edit the configuration in `main.py` to set your desired image path, keywords, font settings, and output path.

2. **Run MemeSplicer**:
   ```bash
   python main.py
   ```

3. **Output**: The generated meme will be saved to the specified output path.

## Configuration

- **Image Path**: Path to the source image.
- **Keywords**: List of keywords for generating the meme's catchphrase.
- **Font Path**: Path to the font file used for text.
- **Font Size**: Size of the text on the meme.
- **Text Color**: RGB tuple for the text color.
- **Text Position**: (x, y) coordinates for text placement on the image.
- **Output Path**: Path where the final meme image will be saved.

## Distribution

MemeSplicer can distribute memes to network influencers. Ensure the `network_data.json` file is present and correctly formatted to utilize this feature.

## Logging

MemeSplicer uses Python's logging module to log errors and information. Logs are printed to the console.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. 