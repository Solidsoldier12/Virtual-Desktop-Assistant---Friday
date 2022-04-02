from Friday_GUI import Ui_Friday
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import sys
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def Speak(audio):
    """
    function to enable Friday to speak
    """
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.TaskExe()

    def takeCommand(self):
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

    def wishme(self):
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
        Speak("I am Friday, How may I be of service!")

    def TaskExe(self):
        self.wishme()
        while True:
            query = self.takeCommand()
            if 'how are you' in query:
                Speak('I am fine sir, how are you?')
            elif 'the time' in query:
                hours,minutes = int(datetime.datetime.now().strftime("%H")),datetime.datetime.now().strftime("%M")
                if hours>12:
                    Speak(f"Sir, the time is {hours-12}:{minutes} PM")
                else:
                    Speak(f"Sir, the time is {hours}:{minutes} AM")
            elif 'bye' in query:
                Speak('Bye Sir, see you later, you can call me anytime')
                break
            elif ('open' in query or 'search' in query) and 'youtube' in query:
                query = query.replace("friday","").replace("search","").replace("youtube","").replace("on","").replace("please","").replace("open","")
                url = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(url)
                Speak(f'Searching {query} on youtube')

            elif 'my location' in query or 'where am i' in query:
                Speak("Checking location")
                ip_add = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
                geo_q = requests.get(url)
                geo_d = geo_q.json()
                state = geo_d['city']
                country = geo_d['country']
                op = "https://www.google.com/maps/place/" + state +' , ' + country
                webbrowser.open(op)
                Speak(f"Sir , You Are Now In {state , country} .")

            elif 'google' in query and 'search' in query:
                query = query.replace('search','').replace('google','').replace('please','').replace('on','').replace('friday','').replace('about','')
                pywhatkit.search(query)
                Speak(f'Searching {query} on google')
            elif 'play' in query:
                query = query.replace('friday','').replace('play','').replace('on','').replace('youtube','').replace('song','')
                pywhatkit.playonyt(query)
                Speak(f'Playing {query}')
            elif 'wikipedia' in query:
                query = query.replace('friday','').replace('wikipedia','').replace('search','').replace('on','').replace('about','').replace('in','')
                wiki = wikipedia.summary(query,2)
                Speak(f'According to wikipedia {wiki}')
            elif 'screenshot' in query:
                Speak('Taking Screenshot')
                ss = pyautogui.screenshot()
                Speak('What should I name this file sir?')
                name = self.takeCommand()
                ss.save('D:\OneDrive - miet.ac.in\Pictures\Screenshots\\' + name + '.png')
                Speak('Screenshot Saved sir')
            else:
                query = query.replace('friday', '')
                pywhatkit.search(query)
                Speak(f' This is what I found on the internet about {query}')

startFunctions = MainThread()


class GUI_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.friday_ui = Ui_Friday()
        self.friday_ui.setupUi(self)

        self.friday_ui.pushButton.clicked.connect(self.startFunc)
        self.friday_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.friday_ui.movies_label = QtGui.QMovie('Iron_Template_1.gif')
        self.friday_ui.label.setMovie(self.friday_ui.movies_label)
        self.friday_ui.movies_label.start()

        self.friday_ui.movies_label_2 = QtGui.QMovie('B.G_Template_1.gif')
        self.friday_ui.label_2.setMovie(self.friday_ui.movies_label_2)
        self.friday_ui.movies_label_2.start()

        self.friday_ui.movies_label_3 = QtGui.QMovie('initial.gif')
        self.friday_ui.label_3.setMovie(self.friday_ui.movies_label_3)
        self.friday_ui.movies_label_3.start()

        self.friday_ui.movies_label_4 = QtGui.QMovie('Jarvis_Gui (1).gif')
        self.friday_ui.label_4.setMovie(self.friday_ui.movies_label_4)
        self.friday_ui.movies_label_4.start()

        self.friday_ui.movies_label_6 = QtGui.QMovie('Siri_1.gif')
        self.friday_ui.label_6.setMovie(self.friday_ui.movies_label_6)
        self.friday_ui.movies_label_6.start()

        startFunctions.start()

Gui_App = QApplication(sys.argv)
Gui_Friday = GUI_Start()
Gui_Friday.show()
exit(Gui_App.exec_())