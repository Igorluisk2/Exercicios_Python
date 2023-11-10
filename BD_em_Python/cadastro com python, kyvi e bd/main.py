import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from bd import *

class Deckshop(App):
    
    def build(self):
        show_screen = ScreenManager()
        show_screen.add_widget(Menu(name = 'Tela 01'))
        show_screen.add_widget(Cadastrar(name = 'Tela 02')) # add nome 
        show_screen.add_widget(Editar(name = 'Tela 03'))
        show_screen.add_widget(Excluir(name = 'Tela 04'))
        show_screen.add_widget(Mostrar(name = 'Tela 05'))
        show_screen.current = 'Tela 01'

        return show_screen
    
class Menu(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)

        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 1)
        
        
        self.info = Label(text = "Seja Bem vindo à Deckshop")
        
        self.btn_cadastrar = Button(text = "Cadastrar Produto")
        self.btn_Editar = Button(text = "Editar")
        self.btn_excluir = Button(text = "Excluir")
        self.btn_mostrar = Button(text = "Mostrar")
        self.btn_sair = Button(text = "Sair")
        
        self.btn_cadastrar.bind(on_press = self.show_cadastrar)
        self.btn_Editar.bind(on_press = self.show_editar)
        self.btn_excluir.bind(on_press = self.show_excluir)
        self.btn_mostrar.bind(on_press = self.show_mostrar)
        self.btn_sair.bind(on_press = self.show_sair)
        
        grid.add_widget(self.info)
        grid.add_widget(self.btn_cadastrar)
        grid.add_widget(self.btn_Editar)
        grid.add_widget(self.btn_excluir)
        grid.add_widget(self.btn_mostrar)
        grid.add_widget(self.btn_sair)
        
        layout.add_widget(grid)

        self.add_widget(layout)
        
        
    def show_cadastrar(self, cadastrar):
        self.manager.current = "Tela 02"
        
    def show_editar(self, editar):
        self.manager.current = "Tela 03"
        
    def show_excluir(self, excluir):
        self.manager.current = "Tela 04"
        
    def show_mostrar(self, mostrar):
        self.manager.current = "Tela 05"

    def show_sair(self, sair):
        Deckshop().stop()
        
class Cadastrar(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        self.bd = BancoD()
        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 1)

        self.inp_prod = TextInput(hint_text= "Nome do produto")
        self.inp_quant = TextInput(hint_text= "Quantidade do produto")
        self.btn_cadastrar = Button(text = "Cadastrar Produto")
        self.btn_cadastrar.bind(on_press = self.show_insert)
        self.btn_sair = Button(text = "Sair")
        self.btn_sair.bind(on_press = self.show_sair)
        
        grid.add_widget(self.inp_prod)
        grid.add_widget(self.inp_quant)
        grid.add_widget(self.btn_cadastrar)
        grid.add_widget(self.btn_sair)
        
        layout.add_widget(grid)

        self.add_widget(layout)
        
    def show_sair(self, sair):
        self.manager.current = "Tela 01"
    
    def show_insert(self, insert):
        
        self.bd.insert_table(f"{self.inp_prod.text}", f"{self.inp_quant.text}")

class Editar(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        self.bd = BancoD()
        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 1)
        
        self.inp_id = TextInput(hint_text= "ID", size_hint= (0.3, 0.3))
        self.inp_prod = TextInput(hint_text= "Nome do produto")
        self.inp_quant = TextInput(hint_text= "Quantidade do produto")
        self.btn_procurar = Button(text = "Procurar")
        self.btn_procurar.bind(on_press = self.show_procurar)
        self.btn_Editar = Button(text = "Editar")
        self.btn_Editar.bind(on_press = self.show_editar)
        self.btn_sair = Button(text = "Sair")
        self.btn_sair.bind(on_press = self.show_sair)
        
        grid.add_widget(self.inp_id)
        grid.add_widget(self.inp_prod)
        grid.add_widget(self.inp_quant)
        grid.add_widget(self.btn_procurar)
        grid.add_widget(self.btn_Editar)
        grid.add_widget(self.btn_sair)
        
        layout.add_widget(grid)

        self.add_widget(layout)
        
    def show_sair(self, sair):
        self.manager.current = "Tela 01"
        
    def show_editar(self, update):
        
        self.bd.update_table(f"{self.inp_prod.text}", f"{self.inp_quant.text}", self.inp_id.text)
        
    def show_procurar(self, procurar):
        
        self.bd.select_id_table(self.inp_id.text)
        self.inp_prod.text = f"{self.bd.i}"
        self.inp_quant.text = f"{self.bd.a}"

        
class Excluir(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        self.bd = BancoD()
        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 1)
        
        self.inp_id = TextInput(hint_text= "ID", size_hint= (0.3, 0.3))
        self.inp_prod = TextInput(hint_text= "Nome do produto", readonly=True)
        self.inp_quant = TextInput(hint_text= "Quantidade do produto", readonly=True)
        self.btn_procucar = Button(text = "Procucar")
        self.btn_procucar.bind(on_press = self.show_procurar)
        self.btn_excluir = Button(text = "Excluir")
        self.btn_excluir.bind(on_press = self.show_excluir)
        self.btn_sair = Button(text = "Sair")
        self.btn_sair.bind(on_press = self.show_sair)
        
        grid.add_widget(self.inp_id)
        grid.add_widget(self.inp_prod)
        grid.add_widget(self.inp_quant)
        grid.add_widget(self.btn_procucar)
        grid.add_widget(self.btn_excluir)
        grid.add_widget(self.btn_sair)
        
        layout.add_widget(grid)

        self.add_widget(layout)
        
    def show_sair(self, sair):
        self.manager.current = "Tela 01"
        
    def show_procurar(self, procurar):
        try:
           
            self.bd.select_id_table(self.inp_id.text)
            self.inp_prod.text = f"{self.bd.i}"
            self.inp_quant.text = f"{self.bd.a}"
        except:
            self.inp_prod.text = "Não existe este produto"
            self.inp_quant.text = "Não existe este produto"
            
    def show_excluir(self, excluir):
        
        self.bd.delete(self.inp_id.text)
        
class Mostrar(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        
        self.bd = BancoD()
        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 1)
        
        self.inp_id = TextInput(hint_text= "ID", size_hint= (0.2, 0.2))
        self.inp_prod = TextInput(hint_text= "Nome do produto",  readonly=True)
        self.inp_quant = TextInput(hint_text= "Quantidade do produto",  readonly=True)
        self.btn_mostrar = Button(text = "Mostrar Produto")
        self.btn_mostrar.bind(on_press = self.show_procurar)
        self.btn_sair = Button(text = "Sair")
        self.btn_sair.bind(on_press = self.show_sair)
        
        grid.add_widget(self.inp_id)
        grid.add_widget(self.inp_prod)
        grid.add_widget(self.inp_quant)
        grid.add_widget(self.btn_mostrar)
        grid.add_widget(self.btn_sair)
        
        layout.add_widget(grid)

        self.add_widget(layout)
        
    def show_sair(self, sair):
        self.manager.current = "Tela 01"
        
    def show_procurar(self, procurar):
        try:
            
            self.bd.select_id_table(self.inp_id.text)
            self.inp_prod.text = f"{self.bd.i}"
            self.inp_quant.text = f"{self.bd.a}"
            
        except:
            self.inp_prod.text = "Não existe este produto"
            self.inp_quant.text = "Não existe este produto"
        
if __name__ == '__main__':
    Deckshop().run()