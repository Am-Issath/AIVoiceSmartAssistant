import wikipedia
from listen_speak import speak

# def search_wikipedia(query):
#     try:
#         summary = wikipedia.summary(query, sentences=1)
#         speak(f"Here's a summary from Wikipedia: {summary}")
#         print(f"Here's a summary from Wikipedia: {summary}")
#     except wikipedia.exceptions.DisambiguationError as e:
#         speak("Multiple results found. Please be more specific in your query.")
#         print("Multiple results found. Please be more specific in your query.")
#     except wikipedia.exceptions.PageError as e:
#         speak(f"Sorry, I couldn't find information about {query} on Wikipedia.")
#         print(f"Sorry, I couldn't find information about {query} on Wikipedia.")

# Function to search and retrieve information from Wikipedia
def search_wikipedia(query):
    try:
        # Extract the relevant part of the command for searching on Wikipedia
        search_query = query.lower().replace("search", "").replace("look up", "").replace("information", "").replace("tell me", "").strip()
        if search_query:
            summary = wikipedia.summary(search_query, sentences=1)
            speak(f"Here's a summary from Wikipedia: {summary}")
            print(f"Here's a summary from Wikipedia: {summary}")
        else:
            speak("I'm sorry, I couldn't understand your question properly.")
            print("I'm sorry, I couldn't understand your question properly.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found. Please be more specific in your query.")
        print(f"Multiple results found. Please be more specific in your query.")
    except wikipedia.exceptions.PageError as e:
        speak(f"Sorry, I couldn't find information about {query} on Wikipedia.")
        print(f"Sorry, I couldn't find information about {query} on Wikipedia.")
