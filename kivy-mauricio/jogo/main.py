# Importando as bibliotecas necessárias do Kivy e outras
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint
from logica import AdivinheNumero  # Importando a lógica do jogo a partir de um módulo chamado logica

# Definindo a classe para a tela principal do menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        # Criando um layout de caixa vertical
        layout = BoxLayout(orientation='vertical')
        # Criando botão para iniciar o jogo
        self.play_button = Button(text='Jogar', font_size=20)
        self.play_button.bind(on_press=self.switch_to_game)  # Vinculando a função ao pressionar o botão
        # Criando botão para sair da aplicação
        self.exit_button = Button(text='Sair', font_size=20)
        self.exit_button.bind(on_press=App.get_running_app().stop)  # Vinculando a função ao pressionar o botão
        # Adicionando os widgets ao layout
        layout.add_widget(self.play_button)
        layout.add_widget(self.exit_button)
        # Adicionando o layout à tela
        self.add_widget(layout)

    # Função para mudar para a tela de jogo
    def switch_to_game(self, *args):
        self.manager.current = 'game'  # Mudando para a tela de jogo


# Definindo a classe principal da aplicação
class AdivinheAPP(App):
    # Função para construir a interface gráfica
    def build(self):
        # Criando o gerenciador de telas
        screen_manager = ScreenManager()
        # Adicionando a tela principal ao gerenciador
        screen_manager.add_widget(MainMenu(name='main_menu'))
        # Adicionando a tela de jogo ao gerenciador
        screen_manager.add_widget(AdivinheNumero(name='game'))
        # Retornando o gerenciador como a interface gráfica da aplicação
        return screen_manager

# Executando a aplicação se o script for executado diretamente
if __name__ == '__main__':
    AdivinheAPP().run()