# timer_and_youtube_functions.py

import time
import webbrowser

def set_timer(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    print("Timer expired. Time's up!")

def play_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    try:
        webbrowser.open(url, new=2)
        print(f"Now playing {query} on YouTube.")
    except Exception as e:
        print(f"Error playing YouTube video: {e}")
        print("Sorry, there was an error playing the song on YouTube.")
