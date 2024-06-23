from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MeuApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Botão 1'))
        layout.add_widget(Button(text='Botão 2'))
        layout.add_widget(Button(text='Botão 3'))
        layout.add_widget(Button(text='Botão 4'))
        return layout

if __name__ == '__main__':
    MeuApp().run()
