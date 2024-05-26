# Import the SpeechGraph class from scrapegraphai.graphs module
from scrapegraphai.graphs import SpeechGraph

# Configuration settings for the speech synthesis graph
graph_config = {
    "llm": {
        "api_key": "YOUR_OPENAI_API_KEY",  # OpenAI API key for authentication
        "model": "gpt-3.5-turbo",  # Specifies the GPT model version to use
    },
    "tts_model": {
        "api_key": "YOUR_OPENAI_API_KEY",  # API key for the text-to-speech service
        "model": "tts-1-hd",  # Text-to-speech model specification
        "voice": "fable",  # Voice style for the audio output
    },
    "output_path": "audio_summary.mp3",  # File path for the saved audio output
}

# Create an instance of SpeechGraph for audio generation from text
speech_graph = SpeechGraph(
    prompt="Summarize information provided on the website.",  # The AI prompt to process
    source="https://bodrovis.tech",  # URL of the website to summarize
    config=graph_config,  # Apply the specified configuration settings
)

# Execute the speech synthesis process
result = speech_graph.run()

# Print the results to the console
print(result)
