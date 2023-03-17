import speech_recognition as sr
import pyttsx3
import text_analzyer
from gtts import gTTS
import playsound
import time

# def speak(audio):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say(audio)
#     engine.runAndWait()

def speak(text):
    start = time.time()
    start2 = time.time()
    tts = gTTS(text=text, lang='tl')
    filename = 'voice.mp3'
    tts.save(filename)
    print ("Process time[speak_2]: " + str(time.time() - start))
    playsound.playsound(filename)
    print ("Process time[speak]: " + str(time.time() - start))
    

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
    queue = 'sino nag develop'
    start = time.time()
    text_analzyer.token_analyze(queue)
    print ("Process time: " + str(time.time() - start))


if __name__ =='__main__':
    start = time.time()
    take_query()
    print ("Process time[voice_input]: " + str(time.time() - start))
