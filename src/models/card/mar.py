from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class MAR(MDBoxLayout):
    def __init__(self,h,a):
        super().__init__()
        self.orientation = 'vertical'
        conteudo = MDBoxLayout()

    # ---- HORAS -----
        horas = MDLabel(text=h)
        horas.adaptive_height = True
        horas.halign = 'center'
        horas.font_size = '31dp'
        horas.bold = True
        horas.color = [1,1,0,1]
        conteudo.add_widget(horas)

    # ---- ALTURA ----
        altura = MDLabel(text=a)
        altura.adaptive_height = True
        altura.halign = 'center'
        altura.font_size = '31dp'
        altura.bold = True
        altura.color = [1,1,0,1]
        conteudo.add_widget(altura)

    # ----- LISTRA -----
        listra = MDBoxLayout()
        listra.md_bg_color = [1,1,1,0.7]
        listra.size_hint = [0.85,None]
        listra.pos_hint = {'center_x':0.5}
        listra.height = '2dp'

        self.add_widget(conteudo)
        self.add_widget(listra)

        
        