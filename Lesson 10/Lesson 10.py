#Make sure to run: pip install pyttsx3 SpeechRecognition llama-cpp-python
from llama_cpp import Llama
import pyttsx3
import speech_recognition as sr

# Initialize the recognizer and voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 130)  # Set speaking speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use default voice

# Load the LLaMA language model (adjust the path as needed)
LLM = Llama(model_path="llama-2-chat.gguf")

# Step 1: Function to convert speech to text
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""
    
# Step 2: Function to get a smart reply from the LLaMA model
def get_reply(question):
    prompt = f"Q: {question} A:"
    response = LLM(prompt)
    return response["choices"][0]["text"].strip()

# Step 3: Function to make the robot speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
if __name__ == "__main__":
    while True:
        question = get_audio()
        if question.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        elif question:
            reply = get_reply(question)
            print("Bot:", reply)
            speak(reply)
