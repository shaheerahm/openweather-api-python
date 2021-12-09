from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class WeatherGuy(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint =(0.6,0.7)
        self.window.pos_hind = {"center_x": 0.5, "center_y": 0.5}
        
        #add widgets to window
        self.window.add_widget(Image(source="logo.png"))
        return self.window

if __name__ == "__main__":
    SayHello().run()
