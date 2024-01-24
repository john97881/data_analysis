import networkx as nx
import matplotlib.pyplot as plt

# Define symptoms and diagnoses
symptoms = ['Fever', 'Cough', 'Sore Throat', 'Fatigue', 'Headache']
diagnoses = ['Cold', 'Flu']

# Create a directed graph
G = nx.DiGraph()

# Add nodes for symptoms and diagnoses
G.add_nodes_from(symptoms, bipartite=0)
G.add_nodes_from(diagnoses, bipartite=1)

# Define edges between symptoms and diagnoses
edges = [('Fever', 'Cold'), ('Fever', 'Flu'),
         ('Cough', 'Cold'), ('Cough', 'Flu'),
         ('Sore Throat', 'Cold'), ('Sore Throat', 'Flu'),
         ('Fatigue', 'Cold'), ('Fatigue', 'Flu'),
         ('Headache', 'Cold'), ('Headache', 'Flu')]

G.add_edges_from(edges)

# Draw the graph
pos = nx.bipartite_layout(G, symptoms)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray', arrowsize=20)

# Show the plot
plt.title("JPD Diagram for Diagnosing Colds or Flu")
plt.show()

