import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
# Aqui, você importa BoxLayout e kivy.uix.boxlayout.

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
'''Em seguida, cria uma lista de cores, 
que são listas de cores do tipo RGB. 
Finalmente, você faz um loop,
criando um botão btn para cada iteração. '''

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text = f'Este é o botão #{i+1}',
                        background_color=random.choice(colors))
            '''Para tornar as coisas um pouco mais divertidas, 
            você define background_color para uma cor aleatória.'''

            layout.add_widget(btn)
        # Em seguida, adiciona o botão ao seu layout com layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    HBoxLayoutExample().run()
