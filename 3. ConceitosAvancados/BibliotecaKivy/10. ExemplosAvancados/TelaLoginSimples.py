from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Button(text='Login', on_press=self.login))

    def login(self, instance):
        print(f"Username: {self.username.text}, Password: {self.password.text}")

class MeuApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MeuApp().run()
