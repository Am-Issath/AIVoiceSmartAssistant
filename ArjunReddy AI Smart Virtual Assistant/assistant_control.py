# assistant_control_functions.py

import spacy
from listen_speak import listen, speak
from weather import get_weather
from timer_and_youtube import set_timer, play_youtube
from storytelling import tell_story
from wikipedia_search import search_wikipedia
from news import get_latest_news

nlp = spacy.load("en_core_web_md")

# Replace these with actual values or import them from a configuration file
api_key = "f47f465f10c61753b6dcf2da6a219640"  # Replace with OpenWeatherMap API key
lat = 9.317492
lon = 80.399958
news_api_key = "0d2d35cc6e194dd88699a523ecf74c74" # Replace with our News API key
news_source = "google-news"

def stop_assistant(command):
    stop_keywords = ["stop", "bye", "goodbye", "thank you", "see you later"]
    for keyword in stop_keywords:
        if keyword in command:
            return True
    return False

def perform_task(command):
    doc = nlp(command)

    if "weather" in command:
        response = get_weather(api_key, lat, lon)
    elif "set a timer" in command:
        speak("Sure, how many minutes would you like to set the timer for?")
        try:
            minutes = int(listen())
            set_timer(minutes)
            return
        except ValueError:
            response = "Sorry, I didn't catch that. Please say a valid number."
    elif "play" in command and "on youtube" in command:
        song_start_index = command.find("play") + len("play")
        song_end_index = command.find("on youtube")
        song_name = command[song_start_index:song_end_index].strip()
        play_youtube(song_name)
        return
    elif any(keyword in command for keyword in ['funny', 'adventure', 'mystery']):
        story_type = next(keyword for keyword in ['funny', 'adventure', 'mystery'] if keyword in command)
        tell_story(story_type)
        return
    elif any(keyword in command.lower() for keyword in ['search', 'look up', 'information', 'tell']):
        query_start_index = command.lower().find("wikipedia for") + len("wikipedia for")
        query = command[query_start_index:].strip()
        search_wikipedia(query)
        return
    elif "latest news" in command or "what's the latest news" in command:
        get_latest_news(news_api_key, news_source)
        return
    else:
        response = "I'm sorry, I didn't understand that command. Can you please repeat?"

    speak(response)
