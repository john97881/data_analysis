"""
Diamonds Clustering Analysis
This script performs clustering analysis on diamond data. It includes visualizations and comparisons for different combinations of variables.
Disclaimer:
This code is created for an academic task. Use it for educational purposes only.

How to Run:
1. Clone the repository.
2. Open the `diamonds_clustering_analysis.py` file in a Python environment.
3. Run the script.

Author:
[Ioannis Skouras]
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# this line displays plots
plt.ion()

# Load the dataset from the CSV file
diamonds = pd.read_csv("C:\\Users\\User\\Desktop\\My Lessons\\dei computer science\\AI Artificial Inteligence\\assignments\\AI assignment\\archive\\diamonds.csv")

# Function to perform clustering and return clustered data
def perform_clustering(features, num_clusters):
    # Use one-hot encoding for categorical features
    #'num' stands for numeric features and 'cat' stands for categorical features.
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['carat', 'price']),
            ('cat', OneHotEncoder(), ['color', 'clarity', 'cut'])
        ])

    # Apply the preprocessing steps
    X = preprocessor.fit_transform(diamonds[['carat', 'price', 'color', 'clarity', 'cut']])

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    diamonds['cluster'] = kmeans.fit_predict(X)

    # Return the clustered data
    return diamonds[['carat', 'price', 'color', 'clarity', 'cut', 'cluster']]

# List of variable combinations
variable_combinations = [['carat', 'color'], ['clarity', 'color'], ['carat', 'clarity'], ['cut', 'price'],['price','carat'],['price','color'],['clarity','price']]

# Perform clustering and create additional graphs for all variable combinations
for variables in variable_combinations:
    clustering_result = perform_clustering(variables, 3)

    # Display clustering results in tables
    print(f"\nClustering for {', '.join(variables)}:")
    print(clustering_result.head(10))  # Displaying the first 10 rows for brevity
    print(clustering_result['cluster'].unique())


    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(clustering_result[variables[0]], clustering_result[variables[1]], c=clustering_result['cluster'], cmap='viridis', marker='o', label='Cluster')
    plt.title(f'K-means Clustering of Diamonds: {variables[0]} and {variables[1]}')
    plt.xlabel(variables[0])
    plt.ylabel(variables[1])
    plt.legend()
    plt.colorbar(scatter, label='Cluster ID')
    plt.grid(True)
    plt.show()

# Element-wise check for cluster equality
for i in range(len(variable_combinations) - 1):
    for j in range(i + 1, len(variable_combinations)):
        check_result = (perform_clustering(variable_combinations[i], 3)['cluster'] == perform_clustering(variable_combinations[j], 3)['cluster']).all()
        print(f"Clusters for {', '.join(variable_combinations[i])} and {', '.join(variable_combinations[j])} are equal: {check_result}")

# Table for Price in USD, EUR, and GBP
usd_to_eur = 0.90  # Exchange rate: 1 USD to EUR
usd_to_gbp = 0.79  # Exchange rate: 1 USD to GBP

diamonds['price_eur'] = diamonds['price'] * usd_to_eur
diamonds['price_gbp'] = diamonds['price'] * usd_to_gbp

price_comparison = diamonds[['price', 'price_eur', 'price_gbp']]

# Visualize the price comparison
plt.figure(figsize=(8, 6))
plt.plot(price_comparison.index, price_comparison['price'], label='Price (USD)')
plt.plot(price_comparison.index, price_comparison['price_eur'], label='Price (EUR)')
plt.plot(price_comparison.index, price_comparison['price_gbp'], label='Price (GBP)')
plt.title('Price Comparison of Diamonds in USD, EUR, and GBP')
plt.xlabel('Diamond Index')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

print("\nPrice Comparison (USD, EUR, GBP):")
print(price_comparison.head(10))
