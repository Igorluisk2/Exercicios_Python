import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class Bot(App):
    
    def build(self):
        
        layout = BoxLayout(orientation = "vertical")
        grid = GridLayout(cols = 2)
        
        self.img1 = Image(source ='cachorro.jpg', opacity = 0)
        self.img2 = Image(source ='gato.jpg', opacity = 0)
        
        grid.add_widget(self.img1)
        grid.add_widget(self.img2)
        
        self.btn_dog = Button(text = "Cachorro")
        self.btn_cat = Button(text = "Gato")
        
        grid.add_widget(self.btn_dog)
        grid.add_widget(self.btn_cat)
        
        self.btn_dog.bind(on_press = self.doge)
        self.btn_cat.bind(on_press = self.gato)
        
        
        layout.add_widget(grid)
    
        return layout
    def doge(self, img1):
        self.img1.opacity = 1
        self.img2.opacity = 0
        self.btn_dog.background_color = (0, 1, 0, 1)
        self.btn_cat.background_color = (1, 0, 0, 1)
    
    def gato(self, img2):
        self.img2.opacity = 1
        self.img1.opacity = 0
        self.btn_cat.background_color = (0, 1, 0, 1)
        self.btn_dog.background_color = (1, 0, 0, 1)

        
Bot().run()
    
# botaozin.opacity = 0
# size_hint = (0.2, 0.2)
# pos_hint = {'center_x':0.5, 'center_y':0.5}



    #  img = Image('pug-correndo.jpg')
    #     grid.add_widget(img)
        
    #     layout.add_widget(grid)

