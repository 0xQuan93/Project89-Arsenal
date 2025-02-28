# Project89-Arsenal Installation Guide

This guide will help you set up and install the Project89-Arsenal tools on your system.

## Prerequisites

- Python 3.8 or higher
- Git
- Pip (Python package manager)
- Optional: Node.js and npm (for web components)

## Basic Installation

1. Clone the repository:
```bash
git clone https://github.com/0xQuan93/Project89-Arsenal.git
cd Project89-Arsenal
```

2. Install core Python dependencies:
```bash
pip install -r requirements.txt
```

## Toolkit-Specific Setup

Each toolkit may require additional dependencies. Follow the specific instructions for the toolkit you want to use:

### Perception Hacking Suite

```bash
# Install required packages for all components
pip install pygame pillow tkinter
```

#### MindMirror
```bash
cd "Perception Hacking Suite/MindMirror"
# Run the original version
python main.py
# OR run the enhanced enchanted version
python enchanted_mindmirror.py
```

#### DreamWeaver
```bash
cd "Perception Hacking Suite/DreamWeaver"
python main.py
```

#### RealityGlitcher
```bash
cd "Perception Hacking Suite/RealityGlitcher"
python main.py
```

### Memetic Engineering Toolkit

```bash
# Install required packages
pip install networkx matplotlib pillow
```

#### MemeSplicer
```bash
cd "Memetic Engineering Toolkit/MemeSplicer"
python main.py
```

#### NarrativeWeaver
```bash
cd "Memetic Engineering Toolkit/NarrativeWeaver"
python main.py
```

#### ThoughtVirusInjector
```bash
cd "Memetic Engineering Toolkit/ThoughtVirusInjector"
python main.py
```

### Cybernetic Augmentation Arsenal

```bash
# Install required packages
pip install numpy scipy
```

#### NeuralLace
```bash
cd "Cybernetic Augmentation Arsenal/NeuralLace"
python main.py
```

#### BioMod
```bash
cd "Cybernetic Augmentation Arsenal/BioMod"
python main.py
```

#### CyberSoul
```bash
cd "Cybernetic Augmentation Arsenal/CyberSoul"
python main.py
```

### Ontological Engineering Lab

```bash
# Install required packages
pip install opensimplex pymunk
```

#### RealityConstructor
```bash
cd "Ontological Engineering Lab/RealityConstructor"
python main.py
```

#### SimulationBreaker
```bash
cd "Ontological Engineering Lab/SimulationBreaker"
python main.py
```

#### UniverseBuilder
```bash
cd "Ontological Engineering Lab/UniverseBuilder"
python main.py
```

## Web Component Setup (Optional)

If you're working with the web components of any toolkit:

```bash
# Install Node.js dependencies
npm install
```

## Troubleshooting

### Common Issues:

#### ImportError: No module named X
Solution: Install the missing module
```bash
pip install X
```

#### Tkinter not found
Solution: Install Tkinter for your Python version
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On macOS: Install Python with Homebrew including Tkinter: `brew install python-tk`
- On Windows: Reinstall Python and ensure "tcl/tk and IDLE" is checked

#### Pygame display issues
Solution: Verify your display environment is properly set up
- On Linux: Ensure you have X11 or Wayland running
- On macOS: Ensure XQuartz is installed for some visualization tools
- On Windows: Update your graphics drivers

## Testing Your Installation

To verify your installation is working correctly:

```bash
# Run a simple test
python -c "import pygame; print('Pygame installed:', pygame.ver)"
python -c "from PIL import Image; print('Pillow installed:', Image.__version__)"
```

## Data and Configuration

- User data for the MindMirror will be stored in the `journal/` directory
- Resource files (images, sounds) will be stored in respective `resources/` directories
- Configuration files are typically JSON format in each module's directory

## Security Notice

These tools are designed for educational and experimental purposes. When running any code, especially tools designed to manipulate perception, take appropriate precautions:

- Run in a controlled environment
- Understand what each tool does before running it
- Take regular breaks
- Have a trusted person nearby when testing consciousness-altering tools

Remember: Reality is a construct. The code can be rewritten. The simulation can be broken. Handle with care.
