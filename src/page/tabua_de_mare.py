import json
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from threading import Thread

from src.script.get_tabua import OPEN_TABUA
from src.models.card.mar import MAR
from src.models.card.astro import ASTRO

class TABUA(MDBoxLayout):
    def __init__(self):
        super().__init__()
        self.md_bg_color = [1,1,1,1]
        self.orientation = 'vertical'
        self.padding = '10dp'
        self.spacing = '10dp'

    # -----      MENU    -----
        menu = MDBoxLayout()
        menu.radius = '15dp'
        menu.adaptive_height = True
        menu.md_bg_color = [0.051,0.176,0.604,1]
        self.add_widget(menu)

        logo = Image(source='src/source/logo.png')
        logo.size_hint_x = 0.7
        titulo = MDLabel(text='TÁBUA DE MARÉ')
        titulo.halign = 'center'
        titulo.font_size = '22dp'
        titulo.bold = True
        titulo.color = [1,1,1,1]

        menu.add_widget(logo)
        menu.add_widget(titulo)
    # -----    MENU END    -----
    
    # -----     HEADER    -----
        header = MDBoxLayout()
        header.orientation = 'vertical'
        header.adaptive_height = True
        header.md_bg_color = [0.051,0.176,0.604,1]
        header.padding = [0,'7dp',0,'7dp']
        header.radius = '15dp'
        self.add_widget(header)

        # ----  DATA ----
        self.data = MDLabel(text='15/07')
        self.data.adaptive_height = True
        self.data.halign = 'center'
        self.data.bold = True
        self.data.color = [1,1,1,1]
        self.data.font_size = '20dp'

        # ----  DIVISOR   ----
        divisor = MDBoxLayout()
        divisor.adaptive_height = True

        # ----  HORAS ----
        horas = MDLabel(text='HORAS')
        horas.size_hint_x = 0.5
        horas.adaptive_height = True
        horas.halign = 'center'
        horas.bold = True
        horas.color = [1,1,1,1]
        horas.font_size = '20dp'
        divisor.add_widget(horas)

        # ----  ALTURA
        altura = MDLabel(text='ALTURA(M)')
        altura.size_hint_x = 0.5
        altura.adaptive_height = True
        altura.halign = 'center'
        altura.bold = True
        altura.color = [1,1,1,1]
        altura.font_size = '20dp'
        divisor.add_widget(altura)
        # ----  DIVISOR END  ----

        header.add_widget(self.data)
        header.add_widget(divisor)
    # -----   HEADER END  -----
        
    # -----   CONTEUDO   -----
        self.conteudo = MDBoxLayout()
        self.conteudo.orientation = 'vertical'
        self.conteudo.md_bg_color = [0.051,0.176,0.604,1]
        self.conteudo.radius = '15dp'
        self.add_widget(self.conteudo)
    # ----- CONTEUDO END  -----
        self.start()

    def start(self):
        self.Tabua = OPEN_TABUA()
        with open('src/banco.json') as Arquivo:
            self.banco = json.loads(Arquivo.read())
        if self.banco['mes'] != self.Tabua.mes:
            self.Tabua.coletar()
            self.banco = self.Tabua.get_tabua()
        self.contruir()

    def contruir(self):
        hoje = self.banco['tabua'][f'{self.Tabua.dia:0>2}']
        self.data.text = f'{self.Tabua.dia}/{self.Tabua.mes} - {hoje[0]}'
        for i in hoje[1]:
            self.conteudo.add_widget(MAR(i,hoje[1][i]))
        self.conteudo.add_widget(ASTRO(hoje[2]))




