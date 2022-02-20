import wikipedia
import webbrowser
import pyttsx3  # for using the text to speech engine
import speech_recognition as sr
import datetime  # for using date, time, seconds, minutes ,hours etc
import os

engine = pyttsx3.init("sapi5")  # microsoft text to speech API
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def wishme():
    """
    function to Make Yui wish you as per time of day
    """
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello Sir, I am Friday, How may I be of service!")


def takeCommand():
    """
    It takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)
        print(
            "Sorry, I didn't get it, could you say it one more time?"
        )  # This will be printed in case of improper voice
        speak("Sorry, I didn't get it, could you say it one more time?")
        return "None"  # None string will be returned
    return query


def speak(audio):
    """
    function to enable Yui to speak
    """
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
        #elif 'play music' in query:
        #    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #    songs = os.listdir(music_dir)
        #    print(songs)
        #    os.startfile(os.path.join(music_dir, songs[0])) # To open a file on your system
        elif "the time" in query:
            hours,minutes = int(datetime.datetime.now().strftime("%H")),datetime.datetime.now().strftime("%M")
            if hours>12:
                print(f"Sir, the time is {hours-12}:{minutes} PM")
                speak(f"Sir, the time is {hours-12}:{minutes} PM")
            else:
                print(f"Sir, the time is {hours}:{minutes} AM")
                speak(f"Sir, the time is {hours}:{minutes} AM")
        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)