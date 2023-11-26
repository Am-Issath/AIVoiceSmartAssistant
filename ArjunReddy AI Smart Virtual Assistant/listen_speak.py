# listening_and_speaking_functions.py

import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("Recognized:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return "Sorry, I couldn't understand."
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
        return f"Error with the speech recognition service: {e}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
