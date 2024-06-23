from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TouchWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)

class MeuApp(App):
    def build(self):
        layout = FloatLayout()
        layout.add_widget(TouchWidget())
        return layout

if __name__ == '__main__':
    MeuApp().run()
