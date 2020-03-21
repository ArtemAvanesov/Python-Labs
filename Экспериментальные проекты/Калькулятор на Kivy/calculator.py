from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)

class MyApp(App):
    def build(self):
        self.fl = FloatLayout(size = (400,500), id = "0")

        self.fl.add_widget(Button(text = "0",
        id = "btn1",
        background_color = [0,1,0,1],
        font_size = 30,
        size_hint = (0.98, 0.18),
        pos = (4,405)))

        self.fl.add_widget(Button(text = "1",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (4,305),
        #on_press = self.click_btn_one
        ))
        
        self.fl.add_widget(Button(text = "2",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (104,305)))

        self.fl.add_widget(Button(text = "3",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (204,305)))

        self.fl.add_widget(Button(text = "/",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (304,305)))

        self.fl.add_widget(Button(text = "4",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (4,205)))

        self.fl.add_widget(Button(text = "5",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (104,205)))

        self.fl.add_widget(Button(text = "6",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (204,205)))

        self.fl.add_widget(Button(text = "x",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (304,205)))

        self.fl.add_widget(Button(text = "7",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (4,105)))

        self.fl.add_widget(Button(text = "8",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (104,105)))

        self.fl.add_widget(Button(text = "9",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (204,105)))

        self.fl.add_widget(Button(text = "-",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (304,105),
        on_press = self.click_btn_minus))
        
        self.fl.add_widget(Button(text = "0",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (4,5)))

        self.fl.add_widget(Button(text = ".",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (104,5)))

        self.fl.add_widget(Button(text = "+",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (204,5),
        on_press = self.click_btn_plus))

        self.fl.add_widget(Button(text = "=",
        font_size = 30,
        size_hint = (0.23, 0.18),
        pos = (304,5),
        on_press = self.click_btn_minus))

        return self.fl
        
    def click_btn_plus(self, instance):
        instance.background_normal = ''
        instance.background_color = [1,0,0,1]

    def click_btn_minus(self, instance):
        instance.background_normal = ''
        instance.background_color = [1,0,0,1]

    def click_btn_one(self, instance):
        instance.background_normal = ''
        self.fl.ids['btn1'].text = '1'

if __name__ == "__main__":
    MyApp().run()