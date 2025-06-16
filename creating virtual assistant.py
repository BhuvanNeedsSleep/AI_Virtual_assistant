import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Increase the duration and experiment with different values
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand you.")
    except sr.RequestError:
        print("Sorry, I'm having trouble accessing the Google Speech Recognition service.")
    
    return ""


def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def process_command(command):
    command = command.lower()

    if "search for" in command:
        search_query = command[command.index("search for") + len("search for"):].strip()
        search(search_query)
    elif "hello" in command:
        speak("Hello there!")
    elif "how are you" in command:
        speak("I'm doing well, thank you!")
    elif "goodbye" in command:
        speak("Goodbye!")
        exit()

    else:
       
        speak("Sorry, I could not understand you.")




# Main program loop
while True:
    command = listen()
    if command == "":
        # If the user didn't say anything, continue listening
        continue
    elif command.lower() == "exit":
        # If the user says "exit", break the loop and exit the program
        speak("Goodbye!")
        break
    else:
        process_command(command)
