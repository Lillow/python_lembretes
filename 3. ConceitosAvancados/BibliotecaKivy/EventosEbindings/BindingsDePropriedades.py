from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='0')
        slider = Slider(min=0, max=100)
        slider.bind(value=self.on_value_change)
        layout.add_widget(self.label)
        layout.add_widget(slider)
        return layout

    def on_value_change(self, instance, value):
        self.label.text = str(int(value))

if __name__ == '__main__':
    MeuApp().run()
