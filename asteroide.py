
import requests

key_url = "1VMOiac1Qv0903cFqKB2xiID5zRmmZvl0sX4PJY9"
data_from = "2020-09-07"
date_to = "2020-09-08"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={data_from}&end_date={date_to}&api_key={key_url}"
print (url)

response = requests.get(url)
data_frame_aste = response.json()

for date, asteroids in data_frame_aste["near_earth_objects"].items():
    for asteroid in asteroids:
        print(f"- {asteroid['name']}:")
