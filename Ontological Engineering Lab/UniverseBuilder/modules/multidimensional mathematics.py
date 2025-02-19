import numpy as np

def generate_hypercube(dimension):
    """Generates the vertices of a hypercube in the specified dimension."""
    vertices = np.array([[int(bin(i)[2:].zfill(dimension)[j]) for j in range(dimension)] for i in range(2**dimension)])
    return vertices

if __name__ == "__main__":
    # Example usage
    dimension = 4
    vertices = generate_hypercube(dimension)
    print(vertices)