
from kivy.app import App
from kivy.uix.widget import Widget

class UI(Widget):
    pass

class UIApp(App):
    def build(self):
        return UI()

if __name__ == '__main__':
    UIApp().run()