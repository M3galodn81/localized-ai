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

class WelcomeScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class SettingScreen(Screen):
    pass
 
class GABAYApp(App):

    def build(self):
        sm =ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcomeScreen'))
        sm.add_widget(MainScreen(name='mainScreen'))
        sm.add_widget(SettingScreen(name='settingScreen'))
        return sm

if __name__ == "__main__":
    GABAYApp().run()
