import copy

def clone_consciousness(digital_consciousness):
    """Creates a clone of the digital consciousness."""
    cloned_consciousness = copy.deepcopy(digital_consciousness)
    return cloned_consciousness

if __name__ == "__main__":
    # Example usage
    digital_consciousness = np.load("digital_consciousness.npy")
    cloned_consciousness = clone_consciousness(digital_consciousness)
    np.save("cloned_consciousness.npy", cloned_consciousness)