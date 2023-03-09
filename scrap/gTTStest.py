import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='tl')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

speak("hello tim")