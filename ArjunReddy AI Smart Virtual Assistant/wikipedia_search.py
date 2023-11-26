# wikipedia_functions.py

import wikipedia

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=1)
        print(f"Here's a summary from Wikipedia: {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple results found. Please be more specific in your query.")
    except wikipedia.exceptions.PageError as e:
        print(f"Sorry, I couldn't find information about {query} on Wikipedia.")
