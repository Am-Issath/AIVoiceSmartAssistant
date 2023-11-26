# storytelling_functions.py

import random

def tell_story(story_type):
    try:
        stories = {
            'funny': ["Why did the tomato turn red? Because it saw the salad dressing!",
                     "What do you call fake spaghetti? An impasta!",
                     "Why did the bicycle fall over? Because it was two-tired!"],
            'adventure': ["In a land of dragons and magic, a brave knight set out on a quest to save the kingdom.",
                          "Deep in the jungle, an explorer discovered a hidden treasure, but not without facing wild animals and traps.",
                          "On a spaceship traveling through the galaxy, a group of astronauts encountered mysterious alien creatures."],
            'mystery': ["In a small town, a detective was called to solve a puzzling case of a missing diamond.",
                        "Late at night, strange things started happening in an old mansion, and a detective was determined to uncover the mystery.",
                        "On a foggy day, a group of friends stumbled upon a hidden map leading to a mysterious treasure."]
        }

        story = random.choice(stories.get(story_type, ["I'm sorry, I don't have a story of that type."]))
        print(story)
        print("I hope you enjoyed the story. Do you want to hear another one?")

    except Exception as e:
        print(f"An error occurred while telling the story: {e}")
