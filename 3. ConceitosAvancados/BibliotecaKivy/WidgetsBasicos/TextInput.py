from kivy.app import App
from kivy.uix.textinput import TextInput

class MeuApp(App):
    def build(self):
        return TextInput(text='Digite aqui')

if __name__ == '__main__':
    MeuApp().run()
