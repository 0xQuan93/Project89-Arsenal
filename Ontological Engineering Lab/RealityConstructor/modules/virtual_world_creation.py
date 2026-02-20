import opensimplex

def generate_terrain(width, height, seed):
    """Generates a terrain using OpenSimplex noise."""
    gen = opensimplex.OpenSimplex(seed)
    terrain = [[gen.noise2d(x / width, y / height) for x in range(width)] for y in range(height)]
    return terrain

if __name__ == "__main__":
    # Example usage
    width = 512
    height = 512
    seed = 42
    terrain = generate_terrain(width, height, seed)
    # Visualize terrain (using matplotlib or other libraries)
    #...