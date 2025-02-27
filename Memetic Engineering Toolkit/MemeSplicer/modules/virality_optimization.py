import networkx as nx
import tkinter as tk
from tkinter import ttk

class NetworkAnalyzer:
    def __init__(self, network_data):
        if not network_data:
            raise ValueError("Network data cannot be empty")
        self.graph = nx.Graph(network_data)

    def analyze(self):
        # Calculate multiple centrality metrics
        degree_cent = nx.degree_centrality(self.graph)
        betweenness_cent = nx.betweenness_centrality(self.graph)
        eigenvector_cent = nx.eigenvector_centrality(self.graph, max_iter=1000)

        # Combine metrics for ranking
        influencer_scores = {}
        for node in self.graph.nodes():
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

# Function to create a cyberpunk style window
# GUI logic is separated from data processing

def create_cyberpunk_window(influencers):
    root = tk.Tk()
    root.title("Cyberpunk Influencers")
    root.geometry("400x300")
    root.configure(bg="#0f0f0f")  # Dark background

    style = ttk.Style()
    style.configure("TLabel", background="#0f0f0f", foreground="#39ff14", font=("Courier", 12))

    title_label = ttk.Label(root, text="Top Influencers", style="TLabel")
    title_label.pack(pady=10)

    for influencer, metrics in influencers.items():
        influencer_text = f"{influencer}: {metrics['total_score']:.2f}"
        label = ttk.Label(root, text=influencer_text, style="TLabel")
        label.pack(anchor="w", padx=20)

    root.mainloop()

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
    analyzer = NetworkAnalyzer(network_data)
    influencers = analyzer.analyze()
    create_cyberpunk_window(influencers)