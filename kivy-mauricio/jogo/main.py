from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint
from logica import AdivinheNumero


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.play_button = Button(text='Jogar', font_size=20)
        self.play_button.bind(on_press=self.switch_to_game)
        self.exit_button = Button(text='Sair', font_size=20)
        self.exit_button.bind(on_press=App.get_running_app().stop)
        layout.add_widget(self.play_button)
        layout.add_widget(self.exit_button)
        self.add_widget(layout)


    def switch_to_game(self, *args):
        self.manager.current = 'game'


class AdivinheAPP(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenu(name='main_menu'))
        screen_manager.add_widget(AdivinheNumero(name='game'))
        return screen_manager
    
    
if __name__ == '__main__':
    AdivinheAPP().run()