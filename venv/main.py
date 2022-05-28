import pyperclip
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout




class TheLabapp(App):
    pass


class Clicker(GridLayout):
    count = 1
    my_text = StringProperty("Start")
    FiveZL = 0
    TenZL = 0
    TwentyZL = 0
    FiftyZL = 0
    def on_button_click_getCoins(self):
        self.count += 1
        self.FiveZL += 1
        self.my_text = f"People:{self.count} ({self.TenZL}*10 {self.TwentyZL}*20 {self.FiftyZL}*50)"

    def on_button_click_getTenZl(self):
        self.count += 1
        self.TenZL += 1
        self.my_text = f"People:{self.count} ({self.TenZL}*10 {self.TwentyZL}*20 {self.FiftyZL}*50)"

    def on_button_click_getTwentyZl(self):
        self.count += 1
        self.TwentyZL += 1
        self.my_text = f"People:{self.count} ({self.TenZL}*10 {self.TwentyZL}*20 {self.FiftyZL}*50)"

    def on_button_getFiftyZl(self):
        self.count += 1
        self.FiftyZL += 1
        self.my_text = f"People:{self.count} ({self.TenZL}*10 {self.TwentyZL}*20 {self.FiftyZL}*50)"

    def on_button_click_copy(self):
        pyperclip.copy(self.my_text)

    def on_button_click_reset(self):
        self.FiveZL = 0
        self.TenZL = 0
        self.TwentyZL = 0
        self.FiftyZL = 0
        self.my_text = f"People:{self.count} ({self.TenZL}*10 {self.TwentyZL}*20 {self.FiftyZL}*50)"




class BoxLayoutExample(BoxLayout):
    pass





TheLabapp().run()