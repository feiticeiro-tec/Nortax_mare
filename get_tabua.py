import requests
import time
import json

def getDay(HTML):
    day = HTML[HTML.index('<div class="celula_dia" >'):]
    day = day[day.index('>')+1:]
    day = day[:day.index('<')]
    day = int(day.strip())
    return day

def getTimerAndNivel(HTML):
    timer_and_nivel = HTML[HTML.index('<div class="celulas_mares">'):]
    timer_and_nivel = timer_and_nivel[timer_and_nivel.index('>')+1:]
    timer_and_nivel = timer_and_nivel.split('</div>')
    lista = []
    for data in timer_and_nivel:
        try:
            info = data[data.index('>')+1:]
            info = info[:info.index('</b')]
            timer,nivel = info.split('<b>')
            lista.append({'Timer':timer.strip(),'Nivel':nivel.strip()})
        except:
            ...
    return lista

def getSunAndMoon(HTML):
    stars = HTML[HTML.index('<div class="celula_astros">'):]
    stars = stars[stars.index('>')+1:stars.index('</div')]
    stars = stars.split('|')
    result  = []
    for star in stars:
        try:
            star = star.replace('<strong>','')
            star = star.replace('</strong>','')
            
            tag,hora = star.split(': ')
            result.append({tag.strip():hora.strip()})
        except:
            ...
    return result

def getDatas():
    timer = time.localtime()
    mes = int(timer.tm_mon)
    ano = int(timer.tm_year)-2000
    url = f'https://surfguru.com.br/previsao/mare/30955/m?mes={mes}&ano={ano}'    
    resp = requests.get(url)
    html = resp.text
    html = html[html.index('<body'):]
    html = html[html.index('<div class="arrudeia_item_previsao">'):]
    html_dias = html.split('<div class="linha_dia">')[1:]
    result = []
    for HTML in html_dias:
        result.append({'article':getTimerAndNivel(HTML),'day':getDay(HTML),'mon':mes,'stars':getSunAndMoon(HTML)})
    return result

def sincronizar():
    try:
        with open('tabua.json') as tabua:
            data = json.loads(tabua.read())
    except:
        with open('tabua.json','w') as tabua:
            tabua.write(json.dumps({'mon':0,'result':[]}))
            data = {"mon":0,"result":[]}

    if data['mon'] != int(time.localtime().tm_mon):
        data['result'] = getDatas()
        data['mon'] = int(time.localtime().tm_mon)
        with open('tabua.json','w') as tabua:
            tabua.write(json.dumps(data))
    return data

def getNow():
    tempo = time.localtime()
    data = sincronizar()
    now = data['result'][(tempo.tm_mday)-1]
    return now



    


