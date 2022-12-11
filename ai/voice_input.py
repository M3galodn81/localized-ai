import speech_recognition as sr
import pyttsx3
import text_analzyer

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")    
            query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", query)
            query = ''
        except KeyboardInterrupt:
            assert True
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return query


def take_query():
    while True:
        # queue = take_command().lower()
        queue = 'what time'
        
        text_analzyer.token_analyze(queue)

if __name__ =='__main__':
    take_query()