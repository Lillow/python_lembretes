from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class MeuApp(App):
    def build(self):
        layout = AnchorLayout()
        layout.add_widget(Button(text='Botão', size_hint=(0.5, 0.5)))
        return layout

if __name__ == '__main__':
    MeuApp().run()
