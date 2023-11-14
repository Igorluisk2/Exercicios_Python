# Importa as classes necessárias do Kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Importa as telas definidas em um arquivo chamado 'telas'
from telas import *

# Define a classe principal da aplicação, que herda de App
class Deckshop(App):
    
    # Método chamado automaticamente para construir a interface gráfica
    def build(self):
        # Cria um gerenciador de telas
        show_screen = ScreenManager()

        # Adiciona as telas ao gerenciador de telas
        show_screen.add_widget(Menu(name='Tela 01'))
        show_screen.add_widget(Cadastrar(name='Tela 02'))  
        show_screen.add_widget(Editar(name='Tela 03'))
        show_screen.add_widget(Excluir(name='Tela 04'))
        show_screen.add_widget(Mostrar(name='Tela 05'))

        # Define a tela atual como 'Tela 01'
        show_screen.current = 'Tela 01'

        # Retorna o gerenciador de telas para ser exibido na interface
        return show_screen

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Cria uma instância da classe Deckshop e inicia a execução da aplicação
    Deckshop().run()
