# main.py

from weather import get_weather, number_to_words
from timer_and_youtube import set_timer, play_youtube
from storytelling import tell_story
from news import get_latest_news
from wikipedia_search import search_wikipedia
from assistant_control import stop_assistant, perform_task
from listen_speak import listen, speak

def virtual_assistant():
    assistant_name = "Arjun Reddy"
    speak(f"Hello! I'm {assistant_name}. How can I assist you today?")

    while True:
        command = listen()

        if stop_assistant(command):
            speak("It's my pleasure, Goodbye!")
            break

        elif "what's your name" in command or "your name" in command:
            speak(f"My name is {assistant_name}.")

        elif any(question_keyword in command for question_keyword in ['how are you', 'how are things', "what's up"]):
            speak("I'm doing well, thank you for asking!")

        else:
            perform_task(command)

if __name__ == "__main__":
    virtual_assistant()
