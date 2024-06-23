from kivy.app import App
from kivy.uix.label import Label

'''
Perceba que todo aplicativo Kivy precisa da subclasseApp 
e da função build(). É aqui que você colocará seu código de interface dou suário 
ou fará chamadas para outras funções que definem seu código de interface do usuário.
'''

class MeuApp(App):
    def build(self):

        '''
        Neste caso, crie um widget do tipo label e passe como parâmetro: 
        text, size_hint, 
        e pos_hint (estes dois últimos argumentos não são obrigatórios).
        '''

        return Label(text = 'Olá, Kivy!',
                size_hint = (.5, .5),
                pos_hint = {'center_x': .5, 'center_y': .5})
        '''
        O comando size_hint informa ao Kivy 
        as proporções a serem usadas 
        ao criar o widget.

        Para isso são necessários dois números:
        O primeiro número (x): refere-se à largura do controle.
        O segundo número (y): refere-se à altura do controle.
        '''

if __name__ == '__main__':
    MeuApp().run()
