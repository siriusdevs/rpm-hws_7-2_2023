import requests

url = 'https://hotels4.p.rapidapi.com/locations/search?query=irkutsks'

headers = {
    'X-RapidAPI-Key' : '62105bc9d7msh30ca44972f28115p1d09a5jsn511d8e8915d5'
}

data = requests.get(url=url, headers=headers).json()

for dct in data['suggestions'][1]['entities']:
    print(dct['name'])


