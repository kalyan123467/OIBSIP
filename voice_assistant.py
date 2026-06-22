import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")

def open_website(site):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "wikipedia": "https://www.wikipedia.org"
    }

    if site in websites:
        webbrowser.open(websites[site])
        speak(f"Opening {site}")
    else:
        speak("Sorry, website not found.")

def assistant():
    speak("Hello! I am your voice assistant.")
    print("Voice Assistant Started")
    print("Commands: time, date, open google, open youtube, open github, open wikipedia, exit")

    while True:
        command = input("Enter Command: ").lower()

        if "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "open" in command:
            site = command.replace("open ", "")
            open_website(site)

        elif "exit" in command:
            speak("Goodbye!")
            print("Assistant Closed")
            break

        else:
            speak("Sorry, I did not understand that command.")

if __name__ == "__main__":
    assistant()
