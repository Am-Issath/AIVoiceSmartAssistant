import time
import webbrowser
import pywhatkit
from listen_speak import speak

# Function to set a timer
def set_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    speak(f"Timer set for {minutes} minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        if remaining_time % 60 == 0:
            speak(f"{remaining_time // 60} minutes remaining.")
        time.sleep(1)

    speak("Timer expired. Time's up!")

# Modify the set_timer function to store the end_time globally
end_time = 0  # Initialize end_time globally

# Add a simplified check_timer_status function
def check_timer_status():
    remaining_time = int(end_time - time.time())
    speak(f"The timer has {remaining_time // 60} minutes and {remaining_time % 60} seconds remaining.")


# def play_youtube(query):
#     url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
#     try:
#         webbrowser.open(url, new=2)
#         print(f"Now playing {query} on YouTube.")
#     except Exception as e:
#         print(f"Error playing YouTube video: {e}")
#         print("Sorry, there was an error playing the song on YouTube.")

# Function to play a song on YouTube
def play_youtube(query):
    try:
        pywhatkit.playonyt(query)
        speak(f"Now playing {query} on YouTube.")
    except Exception as e:
        print(f"Error playing YouTube video: {e}")
        speak("Sorry, there was an error playing the song on YouTube.")
