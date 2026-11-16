# Jarvis – Voice-Controlled Desktop Assistant

Jarvis is a beginner-friendly Python voice assistant that listens for a wake word and performs tasks based on voice commands.

This project was built to practise Python programming, speech recognition, text-to-speech and working with external libraries.

## Features

- Wake-word detection using the keyword "Hello".
- Voice responses using text-to-speech.
- Voice-controlled website navigation.
- Open Google, Facebook, Instagram and YouTube.
- Play selected songs using a custom music library.
- Basic error handling for unclear voice commands.

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- Webbrowser

## Project Structure

```text
Mega project/
│
├── main.py
├── musicLibrary.py
├── README.md
└── .gitignore
```

## Installation

Install the required Python libraries:

```bash
pip install SpeechRecognition PyAudio pyttsx3
```

## How to Run

1. Open the project folder in VS Code.
2. Activate your virtual environment.
3. Run the following command:

```bash
python main.py
```

4. Say "Hello" to activate the assistant.
5. Wait for its response and give a voice command.

## Example Commands

- Hello → Activate the assistant.
- Open Google
- Open Facebook
- Open Instagram
- Open YouTube
- Play Baat
- Play Mix
- Play Shining

## Current Limitations

- Speech recognition requires an internet connection.
- Voice recognition accuracy depends on microphone quality and surrounding noise.
- Music playback is limited to songs configured in `musicLibrary.py`.

## Project Status

Version 1.0 – Initial learning project.