# Import the SearchGraph class from scrapegraphai.graphs
from scrapegraphai.graphs import SearchGraph

# Configuration settings for the scraper graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specifies the large language model to use
        "temperature": 0,  # Temperature controls randomness; 0 makes it deterministic
        "format": "json",  # Output format is set to JSON
        "base_url": "http://localhost:11434",  # Base URL where the Ollama server is running
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specifies the embedding model to use
        "temperature": 0,  # Keeps the generation deterministic
        "base_url": "http://localhost:11434",  # Base URL for the embeddings model server
    },
    "verbose": True,  # Enables verbose output for more detailed log information
}

# Create an instance of SearchGraph for specific search query
search_graph = SearchGraph(
    prompt="List me the best pizzerias in Riga",  # The AI prompt specifies what to find
    config=graph_config,  # Uses predefined configuration settings
)

# Execute the search process using the SearchGraph instance
result = search_graph.run()

# Print the results to the console
print(result)


# {
#     "best_pizzerias": [
#         {
#             "name": "Pizzaiolo",
#             "rating": 4.5,
#             "address": "Krišjāņa Valdemāra iela 13, Rīga",
#         },
#         {"name": "Pizza Marvella", "rating": 4.2, "address": "Skārņu iela 55, Rīga"},
#         {"name": "La Biga", "rating": 4.1, "address": "Kronvalda iela 10, Rīga"},
#         {"name": "Pizzeria Riga", "rating": 4.5, "address": "Riga, Latvia"},
#     ]
# }
