from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

class GabayApp(App):
    def build(self):
        button = Button(text='Hello')
        return button

if __name__ == "__main__":
    GabayApp().run()