import speech_recognition as sr 
import pyttsx3
import pyaudio
import webbrowser

# pip install SpeechRecognition
# pip install pyttsx3
# pip install pyaudio
# pip install webbrowser

r = sr.Recognizer()

engine = pyttsx3.init()

def recog():
    with sr.Microphone(2) as source:
        engine.say("Speak Now")
        print("Speak Now : ")
        engine.runAndWait()
        r.energy_threshold = 8000
        audio = r.listen(source)

        try:
            text = str(r.recognize_google(audio,language="fil-PH")).lower()
            # text = ('mag google ka').lower()
            print(text)

            if text == "mag google ka": # <----------
                webbrowser.open("www.google.com")
            elif text == "gusto ko manood sa youtube": #<---------
                webbrowser.open("www.youtube.com") 

            recog()

        except:
            print("I Don't Recognize The Audio")
            pass

recog()