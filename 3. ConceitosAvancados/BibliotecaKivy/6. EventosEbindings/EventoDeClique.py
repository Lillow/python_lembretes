from kivy.app import App
from kivy.uix.button import Button

class MeuApp(App):

    def build(self):
        button = Button(text='Fala Galera',
                        size_hint = (.5, .5),
                        pos_hint = {'center_x': .5, 'center_y': .5})
        button.bind(on_press = self.on_press_button)
        
        return button
    
    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    MeuApp().run()
