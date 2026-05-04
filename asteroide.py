
import requests

key_url = "1VMOiac1Qv0903cFqKB2xiID5zRmmZvl0sX4PJY9"
data_from = "2020-09-07"
date_to = "2020-09-08"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={data_from}&end_date={date_to}&api_key={key_url}"

response = requests.get(url)
data_frame_aste = response.json()

nome_asteroide = []
potencialmente_perigoso =  []
corpo_orbitando = []


for date, asteroids in data_frame_aste["near_earth_objects"].items():
    for asteroid in asteroids:
       nome_asteroide.append(asteroid['name'])
       potencialmente_perigoso.append(asteroid['is_potentially_hazardous_asteroid'])

for date,objeto_planet in data_frame_aste['near_earth_objects'].items():
    for asteroide in objeto_planet:
        for close_approach in asteroide['close_approach_data']:
             corpo_orbitando = {close_approach['orbiting_body']}
      
print(f"O nome do asteroide : {nome_asteroide}")
print(f"O asteroide é potencialmente perigoso :{potencialmente_perigoso}")
print(f"O corpo que o asteroide está orbitando é: {corpo_orbitando}")
     
           