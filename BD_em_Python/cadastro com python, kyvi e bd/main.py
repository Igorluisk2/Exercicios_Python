import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from bd import *




class deckshop(App):
    Layout = BoxLayout(orientation = "vertical")
    grid = GridLayout(cols = 1)
    
    self.info = Label(text = "Bem vindo a deckshop")
    grid.add_widget(self.info)
    
    self.inp_prod = TextInput(TextInput)
    grid.add_widget(self.inp_prod)