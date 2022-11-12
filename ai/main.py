from gtts import gTTS
from playsound import playsound
import random, os, datetime, string
import speech_recognition as sr

def get_random_string(length:int):
    letters = string.ascii_lowercase
    result_string = ''.join(random.choice(letters) for _ in range(length))
    return result_string

def bigkas(args): # TTS (Tagalog)
    tts = gTTS(text=args,lang='tl')
    random_string = get_random_string(4)
    audio_file = os.path.dirname(random_string)+random_string+'-audio.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(args)
    os.remove(audio_file)

def oras():
    hour = datetime.datetime.now() 
    time = datetime.datetime.now().strftime('%I %M')
    if hour >=0 and hour < 12: #if AM or PM
        meridiem = 'AM'
    meridiem = 'PM'

    bigkas(f'Ang oras ngayon ay {time} {meridiem}')

while True:
    with sr.Microphone() as source: #if mircophone detects sound
        print('nakikinig')
        audio = sr.Recognizer().listen(source)
        try:
            queue = sr.Recognizer().recognize_google(audio, language='tl')
            salita = str(queue).lower

            if 'kamusta' in salita and 'ka' in salita: # kamusta ka function
                bigkas('okay lang po')
                print('kamusta')
                continue 
            
            if 'anong' in salita and 'oras' in salita: #anong oras function
                oras()
                print(f'oras')
                continue
            
        #     print(f'{salita}')

        except Exception as e:
            print(e)
            continue
