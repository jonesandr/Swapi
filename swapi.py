
import requests

data = requests.get('https://swapi.dev/api/films').json( )

peliculas = 0
for i in data['results']:
  for j in i['planets']:
    r = requests.get(j).json( )
    if r['climate'] == 'arid':
      peliculas += 1
      break


wookies = 0
for i in data['results'][-1]['characters']:
  r = requests.get(i).json()
  if 'https://swapi.dev/api/species/3/' in r['species']:
    wookies += 1


aeronave = {'nombre':'', 'largo':0}
data = requests.get('https://swapi.dev/api/starships/').json( )
for i in data['results']:
  largo = float(i['length'].replace(',','.'))
  if aeronave['largo'] < largo:
    aeronave['nombre'] = i['name']
    aeronave['largo'] = largo

print('¿En cuántas películas aparecen planetas cuyo clima sea árido?')
print(peliculas)
print('¿Cuántos Wookies aparecen en la sexta película?')
print(wookies)
print('¿Cuál es el nombre de la aeronave más grande en toda la saga?')
print(aeronave)