import speech_recognition as sr
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    speak("Hello")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")    
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query

def take_query():
    while True:
        queue = take_command().lower()
        # queue = 'hello'
        if 'hello' in queue: # kamusta ka function
            speak('kamusta')
            continue 
            
        if ('anong' in queue) and ('oras' in queue): #anong oras function
            speak(f'oras')
            continue
        
if __name__ =='__main__':
    take_query()