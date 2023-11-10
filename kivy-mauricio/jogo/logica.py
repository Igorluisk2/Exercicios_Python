# Importando as bibliotecas necessárias do Kivy e outras
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint

# Definindo a classe para a tela do jogo
class AdivinheNumero(Screen):
    def __init__(self, **kwargs):
        super(AdivinheNumero, self).__init__(**kwargs)
        
        # Criando um layout de caixa vertical
        layout = BoxLayout(orientation='vertical')
        
        # Criando um rótulo para exibir mensagens de resultado
        self.result_label = Label(text='Digite um número entre 1 e 100', font_size=20, size_hint_y=None, height=50)
        
        # Criando uma caixa de entrada de texto para o usuário inserir palpites
        self.input_text = TextInput(multiline=False, font_size=20)
        
        # Criando um botão para enviar os palpites
        self.submit_button = Button(text='Adivinhar', font_size=20)
        self.submit_button.bind(on_press=self.check_guess)  # Vinculando a função ao pressionar o botão
        
        # Criando um botão para resetar o jogo
        self.reset_button = Button(text='Resetar Jogo', font_size=20)
        self.reset_button.bind(on_press=self.reset_game)
        
        # Criando um botão para voltar para o menu principal
        self.menu_button = Button(text='Voltar para o Menu', font_size=20)
        self.menu_button.bind(on_press=self.switch_to_menu)  # Vinculando a função ao pressionar o botão
        
        # Adicionando os widgets ao layout
        layout.add_widget(self.result_label)
        layout.add_widget(self.input_text)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.reset_button)
        layout.add_widget(self.menu_button)  
        
        # Adicionando o layout à tela
        self.add_widget(layout)
        
        # Inicializando o jogo
        self.reset_game()

    # Função para mudar para a tela do menu principal
    def switch_to_menu(self, *args):  
        self.manager.current = 'main_menu'

    # Função para resetar o jogo
    def reset_game(self, *args):
        self.number = randint(1, 100)  # Gerando um novo número aleatório
        self.result_label.text = 'Digite um número entre 1 e 100'
        self.input_text.text = ''  # Limpando a caixa de entrada

    # Função para verificar o palpite do usuário
    def check_guess(self, instance):
        try:
            guess = int(self.input_text.text)
            if guess == self.number:
                self.result_label.text = 'Parabéns! Você acertou!'
            elif guess < self.number:
                self.result_label.text = 'O número é maior'
            elif guess > self.number:
                self.result_label.text = 'O número é menor'
        except ValueError:
            self.result_label.text = 'Por favor, insira um número válido.'

# Classe principal da aplicação
class GuessingGameApp(App):
    def build(self):
        # Criando o gerenciador de telas
        screen_manager = ScreenManager()
        
        # Adicionando a tela do jogo ao gerenciador
        screen_manager.add_widget(AdivinheNumero(name='game'))
        
        # Retornando o gerenciador como a interface gráfica da aplicação
        return screen_manager

# Executando a aplicação se o script for executado diretamente
if __name__ == '__main__':
    GuessingGameApp().run()
