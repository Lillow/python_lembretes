from kivy.app import App
from kivy.uix.image import Image, AsyncImage 
# Nesse código, você importa AsyncImage do kivy.uix.image

class MeuApp(App):
    '''A classe AsyncImage usa muitos parâmetros diferentes, 
    mas o que você deseja usar é source.
    Isso informa ao Kivy qual imagem carregar.'''

    def build(self):
        return AsyncImage(source = 'https://supermariorun.com/assets/img/stage/mario03.png',
                        # Aqui, você passa uma URL qualquer para buscar a imagem.
                size_hint = (1, .5),
                pos_hint = {'center_x': .5, 'center_y': .5})
        
        #return Image(source='imagem.png')

if __name__ == '__main__':
    MeuApp().run()

