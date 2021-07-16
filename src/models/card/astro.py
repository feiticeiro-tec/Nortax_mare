from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton


class cardastro(MDBoxLayout):
    def __init__(self,astros,qual):
        super().__init__()
        self.padding = [5,5,5,5]
    # ---- TEXT ASTRO ----
        texto_astro = Label(text=qual.upper())
        texto_astro.font_size = '28dp'
        texto_astro.bold = True
    # ---- TEXT ASTRO END ----

    # ---- DIVISOR ----
        astro_divisor = MDBoxLayout()
        astro_divisor.orientation = 'vertical'
    # ---- DIVISOR END ----

    # ---- NASCE ----
        astro_nasce = MDBoxLayout()

        # HORAS DO NASCER
        txt_astro_nasce = MDLabel()
        txt_astro_nasce.font_size = '15dp'
        txt_astro_nasce.color = [1,1,1,1]
        txt_astro_nasce.bold = True
        txt_astro_nasce.valign = 'center'
        txt_astro_nasce.halign = 'center'

        # ICON UP
        astro_icon_nasce = MDIconButton()
        astro_icon_nasce.icon = 'src/source/seta_up.png'
        astro_icon_nasce.user_font_size = '4dp'
        astro_icon_nasce.pos_hint = {'center_y':0.5}

        # SET
        astro_nasce.add_widget(txt_astro_nasce)
        astro_nasce.add_widget(astro_icon_nasce)
        astro_divisor.add_widget(astro_nasce)
    # ---- NASCE END ----

    # ---- POE ----
        astro_poe = MDBoxLayout()

        # HORAS DE SE POR
        txt_astro_poe = MDLabel()
        txt_astro_poe.font_size = '15dp'
        txt_astro_poe.valign = 'center'
        txt_astro_poe.halign = 'center'
        txt_astro_poe.color = [1,1,1,1]
        txt_astro_poe.bold = True

        # ICON DOWN
        astro_icon_poe = MDIconButton()
        astro_icon_poe.icon = 'src/source/seta_down.png'
        astro_icon_poe.user_font_size = '4dp'
        astro_icon_poe.pos_hint = {'center_y':0.5}

        # SET
        astro_poe.add_widget(txt_astro_poe)
        astro_poe.add_widget(astro_icon_poe)
        astro_divisor.add_widget(astro_poe)    
    # ---- POE END ----

    # ---- SET TEXT ASTRO AND DIVISOR ----
        self.add_widget(texto_astro)
        self.add_widget(astro_divisor)

        for i in astros:
            if i[:3] == qual:
                if i[-6:] == 'nasce:':
                    txt_astro_nasce.text = astros[i]
                else:
                    txt_astro_poe.text = astros[i]

class ASTRO(MDBoxLayout):
    def __init__(self,astros):
        super().__init__()
        self.add_widget(cardastro(astros,'sol'))
        self.add_widget(cardastro(astros,'lua'))





        
        