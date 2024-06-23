'''Kivy possui uma linguagem de marcação chamada Kv Language 
para definir interfaces de forma mais clara e separada da lógica:
'''

from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        return Button()

if __name__ == '__main__':
    MeuApp().run()