import networkx as nx

def analyze_network(network_data):
    """Analyzes the network data to identify key influencers.
    
    Args:
        network_data (dict): Dictionary representing network connections
        
    Returns:
        dict: Dictionary containing top influencers with their metrics
        
    Raises:
        ValueError: If network_data is empty or invalid
    """
    if not network_data:
        raise ValueError("Network data cannot be empty")
        
    graph = nx.Graph(network_data)
    
    # Calculate multiple centrality metrics
    degree_cent = nx.degree_centrality(graph)
    betweenness_cent = nx.betweenness_centrality(graph)
    eigenvector_cent = nx.eigenvector_centrality(graph, max_iter=1000)
    
    # Combine metrics for ranking
    influencer_scores = {}
    for node in graph.nodes():
        influencer_scores[node] = {
            'degree': degree_cent[node],
            'betweenness': betweenness_cent[node],
            'eigenvector': eigenvector_cent[node],
            'total_score': degree_cent[node] + betweenness_cent[node] + eigenvector_cent[node]
        }
    
    # Get top 10 influencers based on total score
    top_influencers = dict(sorted(
        influencer_scores.items(),
        key=lambda x: x[1]['total_score'],
        reverse=True
    )[:10])
    
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