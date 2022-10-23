from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        l = Label(text="Hello!",
                  font_size=150)

        f.add_widget(l)
        return f

if __name__ == "__main__":
    TutorialApp().run()