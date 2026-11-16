import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Function to process voice commands
def processCommand(command):

    command = command.lower().strip()

    print("Processing command:", command)

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    
    elif command.startswith("play "):
        song = command.replace("play ", "", 1).strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)

        else:
            speak("Sorry, I couldn't find that song in my music library.")
    else:
        speak("Sorry, I don't know that command.")
        print("Command not recognized.")


# Main program
if __name__ == "__main__":

    speak("Initializing Jarvis")

    # Calibrate microphone
    with sr.Microphone() as source:
        print("Calibrating microphone. Please stay quiet...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        recognizer.energy_threshold = 250
        recognizer.dynamic_energy_threshold = True
    print("Calibration complete!")
    speak("Jarvis is ready")

    while True:

        try:
            # Listen for wake word
            print("\nListening for wake word...")

            with sr.Microphone() as source:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=4
                )

            try:
                word = recognizer.recognize_google(audio)
                print("You said:", word)

            except sr.UnknownValueError:
                # Ignore unclear speech while waiting for wake word
                continue

            # Check wake word
            if "hello" in word.lower():

                print("Wake word detected!")

                speak("Yes,how can I help you?")

                time.sleep(1)

                # Listen for command
                print("Jarvis Active! Speak your command...")

                try:
                    with sr.Microphone() as source:
                        audio = recognizer.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=6
                        )

                    command = recognizer.recognize_google(audio)

                    print("Command:", command)

                    # Execute command
                    processCommand(command)

                except (sr.UnknownValueError, sr.WaitTimeoutError):
                    print("Could not understand your command.")
                    speak("Sorry, I couldn't hear you properly. Please repeat your command.")

        except sr.WaitTimeoutError:
            # No speech detected while waiting for wake word
            continue

        except sr.RequestError as e:
            print("Google Speech Recognition error:", e)
            print("Check your internet connection.")

        except KeyboardInterrupt:
            print("\nJarvis stopped.")
            break

        except Exception as e:
            print("Error:", e)