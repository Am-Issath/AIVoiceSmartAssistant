from datetime import datetime
from listen_speak import speak

# Function to get the current time and date
def get_time_and_date(command):
    current_time = datetime.now().strftime("%H:%M")  # Format time as HH:MM
    current_date = datetime.now().strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
    
    if 'time' in command and 'date' in command:
        return f"The current time is {current_time} and the date is {current_date}."
    elif 'time' in command:
        return f"The current time is {current_time}."
    elif 'date' in command:
        return f"The current date is {current_date}."
    else:
        return "I'm sorry, I didn't understand whether you asked for the time or date."

