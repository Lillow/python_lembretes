'''
O Kivy também fornece uma linguagem de design chamada kv, 
que você pode usar com seus aplicativos Kivy. 
A linguagem kv permite separar o design da interface 
e a lógica do aplicativo.

Isso segue o princípio da separação de interesses e 
faz parte do padrão de arquitetura Model-View-Controller.
'''

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):

    def build(self):
        return Button()
    
    def on_press_button(self):
        print('Você apertou o botão!')

if __name__ == '__main__':
    ButtonApp().run()
