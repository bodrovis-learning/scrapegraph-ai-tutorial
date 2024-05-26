# Import the SmartScraperGraph class from scrapegraphai.graphs
from scrapegraphai.graphs import SmartScraperGraph

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

# Create an instance of SmartScraperGraph with specific instructions
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the titles",  # The AI prompt specifies what to extract
    source="https://www.wired.com/",  # URL of the website from which to scrape data
    config=graph_config,  # Uses predefined configuration settings
)

# Execute the scraping process
result = smart_scraper_graph.run()

# Print the results to the console
print(result)

# {
#     "titles": [
#         "Buying Guide: The Best Smart Speakers With Alexa, Google Assistant, and Siri",
#         "Product Review: Insta360 Adds 8K Video to Its 360-Action Camera Hybrid",
#         "Product Review: Samsung’s Flagship QD-OLED Has Glorious, Reflection-Free Picture Quality",
#         "WIRED Classics: Crowdsourcing",
#         "Going Viral: TikTok and the Evolution of Digital Blackface",
#         "We ❤️ Hardware: ‘You Must Believe You Can Repair It’",
#         "Hip Hop's 50th: Hip Hop 2073: A Vision of the Future, 50 Years From Now",
#         "Trending Stories: Science, Gear, Culture",
#         "Videos: Autocomplete Interview, Tech Support",
#     ]
# }
