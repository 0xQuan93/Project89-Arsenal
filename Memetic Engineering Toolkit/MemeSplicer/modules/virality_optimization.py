import networkx as nx

def analyze_network(network_data):
    """Analyzes the network data to identify key influencers."""
    graph = nx.Graph(network_data)
    # Calculate degree centrality
    degree_centrality = nx.degree_centrality(graph)
    # Identify top influencers
    top_influencers = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:10]
    return top_influencers

if __name__ == "__main__":
    # Example usage
    network_data = {
        "Agent1": ["Agent2", "Agent3", "Agent4"],
        "Agent2": ["Agent1", "Agent5"],
        "Agent3": ["Agent1", "Agent6"],
        "Agent4": ["Agent1", "Agent7"],
        "Agent5": ["Agent2"],
        "Agent6": ["Agent3"],
        "Agent7": ["Agent4"]
    }
    influencers = analyze_network(network_data)
    print("Top influencers:", influencers)