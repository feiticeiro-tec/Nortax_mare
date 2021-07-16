from urllib.request import urlopen
import time
import json

class OPEN_TABUA():
    def __init__(self,data=None):
        self.get_hoje(data)
        self.url = f'https://surfguru.com.br/previsao/mare/30955/m?mes={self.mes}&ano={self.ano}'    

    def coletar(self):
        self.conteudo = self.get_conteudo(self.url)
        self.dados = self.get_dict(self.conteudo)
        self.save_file(self.dados)
    
    def get_tabua(self):
        return self.dados

    def get_hoje(self,data=None):
        if data != None:
            self.dia = data[0]
            self.mes = data[1]
            self.ano = data[2]
        else:
            tempo = time.localtime()
            self.dia = int(tempo.tm_mday)
            self.mes = int(tempo.tm_mon)
            self.ano = int(tempo.tm_year)-2000
            return(self.dia,self.mes,self.ano)

    def get_conteudo(self,url):
        resp = urlopen(url).read().decode()
        conteudo = resp[:]
        conteudo = conteudo[conteudo.find('<div class="arrudeia_item_previsao">'):]#pega o inicio e o resto
        conteudo = conteudo[:conteudo.find('</article>')]#inicio ate o fim 
        conteudo = conteudo.replace('\t','')#tira os tab
        conteudo = conteudo.replace('<div class="arrudeia_item_previsao">','')
        conteudo = conteudo.replace('\n','')
        conteudo = conteudo.replace('\r','')
        return conteudo
    
    def get_dict(self,conteudo):
        conteudo = conteudo.split('<div class="linha_dia">')
        dados = {}
        for i in conteudo:
            if len(i)>1:
                dia,dia_semana,resto= self.get_dia(i)
                mar,resto = self.get_mar(resto)
                astro = self.get_astro(resto)
                dados[dia] = [dia_semana,mar,astro]
        dados = {
            "mes":self.mes,
            "tabua":dados
        }
        return dados
        
    def get_dia(self,conteudo):
        resto = conteudo[:] #pega uma copia para dps retirar o elemento
        conteudo = conteudo[conteudo.find('<div class="celula_dia" >'):conteudo.find('</div>')]#pega o conteudo do dia
        resto=resto.replace(conteudo,'')# remove o conteudo do dia do resto
        conteudo = conteudo.replace('<div class="celula_dia" >','') 
        conteudo = conteudo.split('<br/>')
        return(conteudo[0],conteudo[1],resto)

    def get_mar(self,conteudo):
        resto = conteudo[:] #pega uma copia para dps retirar o elemento
        conteudo = conteudo[conteudo.find('<div class="celulas_mares">'):conteudo.find('<div class="celula_astros">')]#pega o conteudo do mar
        resto = resto.replace(conteudo,'')# remove o conteudo do mar
        conteudo= conteudo.replace('<div class="celulas_mares">','')
        conteudo= conteudo.split('</div>')#corta o conteudo por sessão
        mar = {}
        for i in conteudo:#pecorre as sessoes
            dados = i[i.find('>')+1:i.rfind('<')] #pega o conteudo de hora e a altura
            dados = dados.split('<b>')#separa a hora da altura
            if len(dados)>1:#verificar se os dados pegos são o certo
                mar[dados[0]]=dados[1]
        return(mar,resto)

    def get_astro(self,conteudo):
        conteudo = conteudo[conteudo.find('<div class="celula_astros">'):conteudo.rfind('h')+1]
        
        conteudo = conteudo.replace('<div class="celula_astros">','')
    
        conteudo = conteudo.replace('</strong>','')
        
        conteudo = conteudo.split('|')
        astro = {}
        for i in conteudo:
            try:
                estado,horas = i.strip().split(' <strong>')
                astro[estado] = horas
            except:
                ...
        return(astro)

    def save_file(self,dados):
        with open('src/banco.json','w') as Arquivo:
            Arquivo.write(json.dumps(dados))
        


