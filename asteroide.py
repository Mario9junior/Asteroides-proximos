
import requests

key_url = "1VMOiac1Qv0903cFqKB2xiID5zRmmZvl0sX4PJY9"
date_yer = "2020-09-07"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date_yer}&end_date={date_yer}&api_key={key_url}"
print (url)

response = requests.get(url)

data_frame_aste = response.json()

for date, asteroids in data_frame_aste["near_earth_objects"].items():
    for asteroid in asteroids:
        print(f"- {asteroid['name']}:")
