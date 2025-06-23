import pyttsx3

engine = pyttsx3.init()

# Define the function
def speak(message):
    print("Robot will say:", message)
    engine.say(message)
    engine.runAndWait()

# Call the function
speak("Hi there!")
speak("I am learning Python.")
