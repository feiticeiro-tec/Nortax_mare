
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from threading import Thread

from src.page.home import HOME
from src.page.tabua_de_mare import TABUA



class MAIN(MDApp):
    def __init__(self):
        super().__init__()
        self.screen = MDBoxLayout()
        self.screen.md_bg_color=[0.051,0.176,0.604,1]

        self.pages = {'HOME':HOME(self.Goto)}
        Thread(target=self.start).start()
        self.Goto('HOME')

        
    def start(self):
        self.pages['TABUA'] = TABUA()
        
    def Goto(self,Page):
        if Page in self.pages:
            self.screen.clear_widgets()
            self.screen.add_widget(self.pages[Page])

    def build(self):
        return self.screen

MAIN().run()

    
