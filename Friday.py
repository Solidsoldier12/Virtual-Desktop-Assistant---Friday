import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)
#voice_list = [i.id for i in voices]
#print(voice_list)

def Speak(audio):
    """
    function to enable Friday to speak
    """
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

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
        Speak("Sorry, I didn't get it, could you say it one more time?")
        return "None"  # None string will be returned
    return query.lower()

def wishme():
    """
    function to Make Friday wish you as per time of day
    """
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        Speak("Good Morning sir")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon sir")

    else:
        Speak("Good Evening sir")
    Speak("Hello Sir, I am Friday, How may I be of service!")

def TaskExe():
    wishme()
    while True:
        query = takeCommand()
        if 'hello' in query:
            Speak('Hello Sir. How may i help you?')
        elif 'how are you' in query:
            Speak('I am fine sir, how are you?')
        elif 'bye' in query:
            Speak('Bye Sir, see you later, you can call me anytime')
            break
        elif 'search' in query and 'youtube' in query:
            query.replace()
            Speak(f'Searching {query} on youtube')
        elif "the time" in query:
            hours,minutes = int(datetime.datetime.now().strftime("%H")),datetime.datetime.now().strftime("%M")
            if hours>12:
                print(f"Sir, the time is {hours-12}:{minutes} PM")
                speak(f"Sir, the time is {hours-12}:{minutes} PM")
            else:
                print(f"Sir, the time is {hours}:{minutes} AM")
                speak(f"Sir, the time is {hours}:{minutes} AM")

if __name__ == "__main__":
    TaskExe()
    