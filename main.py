# Installing the required libraries and Modules 

# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio
# pip install pywhatkit
# import statements 👇👇👇

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Welcome Sir! I here to help")
engine.say("Please say your command!")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def butler_command():
    try:
        with sr.Microphone() as source:
            print("Listening ....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "pappu" in command:
                command = command.replace("pappu", "")
                print(command) # The result in terminal           
    except:
        pass
    return command

def run_butler():
    command = butler_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing "+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H: %M")
        print(time)
        talk("Current time"+time)

    elif "fact" in command:
        talk(pyjokes.get_joke())
run_butler()