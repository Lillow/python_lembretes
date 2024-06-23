from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MeuApp(App):
    def build(self):
        layout = FloatLayout()
        layout.add_widget(Button(text='Botão', size_hint=(0.3, 0.2), pos_hint={'x': 0.5, 'y': 0.5}))
        return layout

if __name__ == '__main__':
    MeuApp().run()
