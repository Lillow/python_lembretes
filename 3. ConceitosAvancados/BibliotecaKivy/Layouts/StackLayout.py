from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class MeuApp(App):
    def build(self):
        layout = StackLayout()
        for i in range(10):
            layout.add_widget(Button(text=f'Botão {i+1}', size_hint=(0.2, 0.2)))
        return layout

if __name__ == '__main__':
    MeuApp().run()
