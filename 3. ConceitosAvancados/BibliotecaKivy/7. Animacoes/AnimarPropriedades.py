from kivy.app import App
from kivy.animation import Animation
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        button = Button(text='Clique-me')
        button.bind(on_press=self.animate)
        return button

    def animate(self, instance):
        anim = Animation(size=(300, 300), duration=1)
        anim += Animation(size=(100, 100), duration=1)
        anim.start(instance)

if __name__ == '__main__':
    MeuApp().run()
