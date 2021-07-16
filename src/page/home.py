from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.image import Image
import webbrowser

class HOME(MDBoxLayout):
    def __init__(self,Goto):
        super().__init__()
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.pos_hint = {'center_y':0.7}
        self.spacing = 20

    # ----- TITULO ----
        titulo = Image()
        titulo.source = 'src/source/logo.png'
        titulo.pos_hint = {'center_x':0.5}
        titulo.adaptive_height = True
        titulo.allow_stretch = True
        titulo.size_hint = [None,None]
        titulo.size = ['200dp','100dp']

        self.add_widget(titulo)
    # ----- BTN TABUA ----
        btn_tabua = MDFillRoundFlatButton()
        btn_tabua.text = 'TÁBUA DE MARÉ'
        btn_tabua.bind(on_press = lambda obj:Goto('TABUA'))
        btn_tabua.halign = 'center'
        btn_tabua.pos_hint = {'center_x': 0.5}
        btn_tabua.md_bg_color = [1,1,0,1]
        btn_tabua.text_color = [0,0,0.7]
        
        self.add_widget(btn_tabua)
    
    # ----- BTN INSTAGRAM ----
        btn_instagram = MDFillRoundFlatButton()
        btn_instagram.text = 'INSTAGRAM'
        btn_instagram.bind(on_press = lambda obj:webbrowser.open_new('https://www.instagram.com/nortax_noronha/'))
        btn_instagram.halign = 'center'
        btn_instagram.pos_hint = {'center_x': 0.5}
        btn_instagram.md_bg_color = [1,1,0,1]
        btn_instagram.text_color = [0,0,0.7]
        
        self.add_widget(btn_instagram)
        
        