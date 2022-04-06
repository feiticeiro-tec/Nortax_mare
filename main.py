from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from get_tabua import getNow

class Tela(Screen):
    
    def start(self):
        data = getNow()
        for star in data['stars']:
            if star.get('sol nasce'):
                self.ids.stars.ids.sun_up.text = star.get('sol nasce')
            elif star.get('sol se põe'):
                self.ids.stars.ids.sun_down.text = star.get('sol se põe')
            elif star.get('lua nasce'):
                self.ids.stars.ids.moon_up.text = star.get('lua nasce')
            elif star.get('lua se põe'):
                self.ids.stars.ids.moon_down.text = star.get('lua se põe')
        for item in data['article']:
            self.ids.result.add_widget(Linha(item['Timer'],item['Nivel']))
        dia = data['day']
        mes = data['mon']
        texto = f'{dia:0>2}/{mes:0>2}'
        self.ids.dia.text = texto

class Linha(MDBoxLayout):
    hora = StringProperty('')
    nivel = StringProperty('')
    def __init__(self,hora,nivel):
        
        super().__init__()
        self.hora = hora
        self.nivel = nivel
    

class TabuaDeMareApp(MDApp):
    def __init__(self):
        super().__init__()
        self.load_kv('main.kv')
        self.tela = Tela()
        
    def build(self):
        self.tela.start()
        return self.tela

TabuaDeMareApp().run()

    
