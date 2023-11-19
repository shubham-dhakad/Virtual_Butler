# 🗣️ Virtual Butler with Speech Recognition

This Python script introduces a virtual butler capable of speech recognition, providing a hands-free interaction experience. The butler can perform tasks like playing music, telling the current time, and sharing random jokes.

## 🚀 Features

- **Voice Interaction**: Communicate with the butler using speech commands.
- **Music Playback**: Ask the butler to play your favorite music on YouTube.
- **Time Information**: Inquire about the current time with a simple command.
- **Humor Included**: Get a dose of humor by asking for a random joke.

## 🛠️ Installation

Make sure to install the required libraries and modules using the following commands:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
pip install pywhatkit
```

## 🎙️ Usage

Run the script:

```bash
python your_script_name.py
```

## 🤖 How It Works

1. **Initialization**: The butler initializes and welcomes the user.

2. **Command Recognition**: It listens for a command using the microphone.

3. **Trigger Detection**: If the trigger word "pappu" is detected, it processes the command.

4. **Command Execution**:

   - Commands like "play" trigger music playback.
   - "time" fetches the current time.
   - "fact" gets a random joke.

5. **Communication**: The butler communicates through both the console and text-to-speech, providing a seamless user experience.

Feel free to explore the code for more details on how each functionality is implemented.

## 🧑‍💻 Code Overview

```python
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Welcome Sir! I am here to help.")
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
                print(command)  # The result in the terminal
    except:
        pass
    return command

def run_butler():
    command = butler_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("Current time " + time)
    elif "fact" in command:
        talk(pyjokes.get_joke())

run_butler()
```

Copy and paste this code into your `README.md` file to provide a clear overview of the code structure and its main functionalities. Adjust the content as needed for your specific project.

## 🤝 Contribution

Feel free to contribute to enhance the butler's capabilities or fix any issues. Follow these steps:

1. **Fork the repository.**

2. **Create a new branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes and commit them:**

   ```bash
   git commit -m 'Add your feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Submit a pull request.**

Let's make this virtual butler even more amazing together! 🌟

## 🙏 Thank You

Thank you for considering contributing to this project! Your efforts are greatly appreciated. Whether you submit bug reports, feature requests, or code contributions, your contributions make this project better for everyone.

Feel free to reach out if you have any questions or suggestions. Let's continue making this project awesome together!

**Happy Coding!** 🚀
