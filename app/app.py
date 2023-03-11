from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config


from nltk.tokenize import word_tokenize
import datetime


def greeting():
    speak('Hello')

def time_now():
    time = datetime.datetime.now()
    output = time.strftime('%I%M%p')
    print(output)
    speak(output)

def date_now():
    time = datetime.datetime.now()
    output = time.strftime('%B %d %Y')
    print(output)
    speak(output)

def token_analyze(query):
    tokens = word_tokenize(query)
    # tokens = 'Kamusta'
    tokens = [token.lower() for token in tokens]
    print(tokens)

    if 'hello' in tokens:
        print('hello')
        greeting()

    if 'what' in tokens and 'time' in tokens:
        print('time')
        time_now()

    if 'what' in tokens and 'date' in tokens:
        print('date')
        date_now()

    if 'close' in tokens and 'app' in tokens:
        print('exit')
        speak('goodbye')

    if 'kamusta' in tokens:
        speak('Kamusta ka rin')
        print('Tagalog greeting')
    

import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound

# def speak(audio):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say(audio)
#     engine.runAndWait()

def speak(text):
    tts = gTTS(text=text, lang='tl')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        query = ''
        try:
            print("Recognizing")    
            query = r.recognize_google(audio)
            print("the command is printed=", query)
            
        except KeyboardInterrupt:
            assert True
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return query


def take_query():
    
    # queue = take_command().lower()
    queue = 'kamusta'
    token_analyze(queue)
    print('closed program')


Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

class GabayApp(App):
    def build(self):
        button = Button(text='Hello')
        return button

if __name__ == "__main__":
    GabayApp().run()