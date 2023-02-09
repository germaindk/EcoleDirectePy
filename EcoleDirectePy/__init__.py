import json
import requests

s = requests.Session()
s.headers.update({'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,da;q=0.6',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.ecoledirecte.com',
        'referer': 'https://www.ecoledirecte.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-token':''})





def login(user,passwd):
    payload = '''data={
        "uuid": "",
        "identifiant": "USER",
        "motdepasse": "PASSWD ",
        "isReLogin": false
    }
        '''
    payload = payload.replace('USER',user).replace('PASSWD',passwd)
    s.headers.update({'content-length':f'{len(payload)}'})
    r = s.post('https://api.ecoledirecte.com/v3/login.awp?v=4.26.3',data=payload)
    try:

        x = json.loads(r.text['token'])
        s.headers.update({'x-token':f'{x}'})
        global id
        id = json.loads(r.text['data']['accounts'][0]['id'])
        return json.loads(r.text)
    except:
        return json.loads(r.text)

def emploidutemps(date1,date2):
    payload = '''data={
        "dateDebut": "DATE1",
        "dateFin": "DATE2",
        "avecTrous": false
    }'''

    payload = payload.replace('DATE1',date1).replace('DATE2',date2)
    print(payload)
    s.headers.update({'content-length':f'{len(payload)}'})
    r = s.post(f'https://api.ecoledirecte.com/v3/E/{id}/emploidutemps.awp?verbe=get&v=4.26.3',data=payload)
    y = json.loads(r.text)
    return y


def cahierdetexte(date):
    payload = 'data={}'
    s.headers.update({'content-length':f'{len(payload)}'})
    r = s.post(f'https://api.ecoledirecte.com/v3/Eleves/{id}/cahierdetexte/{date}.awp?verbe=get&v=4.26.3',data=payload)
    return json.loads(r.text)

def notes():
    payload = '''data={
        "anneeScolaire": ""
    }'''
    s.headers.update({'content-length':f'{len(payload)}'})
    r = s.post(f'https://api.ecoledirecte.com/v3/Eleves/{id}/notes.awp?verbe=get&v=4.26.3',data=payload)
    return json.loads(r.text)


def messages():
    payload = '''data={
        "anneeMessages": ""
    }'''    
    s.headers.update({'content-length':f'{len(payload)}'})
    r = s.post(f'https://api.ecoledirecte.com/v3/eleves/{id}/messages.awp?force=false&typeRecuperation=received&idClasseur=0&orderBy=date&order=desc&query=&onlyRead=&page=0&itemsPerPage=100&getAll=0&verbe=get&v=4.26.3',data=payload)
    return json.loads(r.text)

def retard():
    payload = '''data={}'''
    r = s.post(f'https://api.ecoledirecte.com/v3/eleves/{id}/viescolaire.awp?verbe=get&v=4.27.0',data=payload)
    return json.load(r.text)