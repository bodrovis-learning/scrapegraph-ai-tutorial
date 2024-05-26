# Import the JSONScraperGraph class from scrapegraphai.graphs
from scrapegraphai.graphs import JSONScraperGraph

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

# Open the demo.json file and read its content into a variable
with open("demo.json", "r", encoding="utf-8") as file:
    text = file.read()

# Create an instance of JSONScraperGraph
json_scraper_graph = JSONScraperGraph(
    prompt="List all the product names along with the average rating based on the reviews. Also include price for every product name.",
    source=text,
    config=graph_config,
)

# Execute the scraping and processing of JSON data
result = json_scraper_graph.run()

# Print the result to the console
print(result)

# {
#     "products": [
#         {"name": "Product A", "average_rating": 4.5, "price": 25.99},
#         {"name": "Product B", "average_rating": 4, "price": 45.5},
#         {"name": "Product C", "average_rating": 4.5, "price": 15.75},
#         {"name": "Product D", "average_rating": 4.5, "price": 29.99},
#         {"name": "Product E", "average_rating": 4.5, "price": 55.0},
#     ]
# }
