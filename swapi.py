import requests

data = requests.get('https://swapi.dev/api/films').json()

count_arid_planets = 0
for i in data['results']:
    for j in i['planets']:
        planet_data = requests.get(j).json()
        if planet_data['climate'] == 'arid':
            count_arid_planets += 1
            break

count_wookies = 0
for i in data['results'][-1]['characters']:
    character_data = requests.get(i).json()
    if 'https://swapi.dev/api/species/3/' in character_data['species']:
        count_wookies += 1

largest_starship = {'name': '', 'length': 0}
data = requests.get('https://swapi.dev/api/starships/').json()
for i in data['results']:
    length = float(i['length'].replace(',', '.'))
    if largest_starship['length'] < length:
        largest_starship['name'] = i['name']
        largest_starship['length'] = length

print('How many movies feature planets with arid climate?')
print(count_arid_planets)
print('How many Wookies appear in the sixth movie?')
print(count_wookies)
print('What is the name of the largest starship in the entire saga?')
print(largest_starship['name'])