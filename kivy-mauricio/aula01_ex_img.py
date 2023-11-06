import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class HelloWorld(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        tamanho = '80'
        self.label = Label(text="Hello World !!", font_size=tamanho)
        self.button = Button(text='Clique', size_hint=(1, 0.5))
        self.button.bind(on_press=self.on_button)
        self.image = None  # Inicialmente, a imagem não está presente na interface
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def on_button(self, instance):
        if self.image is None:
            # Se a imagem não estiver presente, crie o widget de imagem e adicione-o à interface
            self.image = Image(source='kivy-mauricio\deyvin.jpg')
            self.layout.add_widget(self.image)
        else:
            # Se a imagem já estiver presente, remova-a da interface
            self.layout.remove_widget(self.image)
            self.image = None

if __name__ == '__main__':
    HelloWorld().run()
