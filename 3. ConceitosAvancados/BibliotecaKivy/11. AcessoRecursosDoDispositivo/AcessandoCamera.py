from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)
        layout.add_widget(Button(text='Capturar', on_press=self.capture))
        return layout

    def capture(self, instance):
        self.camera.export_to_png('imagem.png')

if __name__ == '__main__':
    MeuApp().run()
