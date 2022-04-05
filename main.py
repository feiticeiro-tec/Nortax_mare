from kivymd.app import MDApp
from kivymd.uix.screen import Screen


class Tela(Screen):
    ...

class TabuaDeMareApp(MDApp):
    def __init__(self):
        super().__init__()
        self.load_kv('main.kv')

    def build(self):
        self.tela = Tela()
        return self.tela

TabuaDeMareApp().run()

    
