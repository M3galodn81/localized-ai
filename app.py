from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class MainWidget(Widget):
    pass

class BoxLayoutExample(BoxLayout):
    pass
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         b1 = Button(text = "A1")
#         b2 = Button(text = "A2")
#         self.add_widget(b1)
#         self.add_widget(b2)


class GABAYApp(App):
    pass
    # def build(self):
    #     f = FloatLayout()
    #     l = Label(text="Hello!",
    #               font_size=150)

    #     f.add_widget(l)
    #     return f

if __name__ == "__main__":
    GABAYApp().run()