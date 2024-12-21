import json
import requests
from geopy import distance
import folium
import os
from dotenv import load_dotenv


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json(
                   )['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def discance_to_coffee(coffee):
    return coffee['distance']


def main():
    load_dotenv()
    apikey = os.getenv('APIKEY')

    with open("coffee.json", "r", encoding="CP1251") as my_file:
        coffees = my_file.read()

    coffees = json.loads(coffees)

    address = input('Где вы находитесь? ')
    address = fetch_coordinates(apikey, address)
    print('Ваши координаты: ', address)
    address = [address[1], address[0]]

    coffee_list = []

    for coffee in coffees:
        address_coffee = [coffee['geoData']['coordinates'][1],
                          coffee['geoData']['coordinates'][0]]
        coffee_new = {}
        coffee_new['title'] = coffee['Name']
        coffee_new['distance'] = distance.distance(address, address_coffee).km
        coffee_new['latitude'] = coffee['geoData']['coordinates'][1]
        coffee_new['longitude'] = coffee['geoData']['coordinates'][0]
        coffee_list.append(coffee_new)

    sorted_coffee_list = sorted(coffee_list, key=discance_to_coffee)
    the_nearest_5_coffee = sorted_coffee_list[:5]

    m = folium.Map([address[0], address[1]], zoom_start=12)

    folium.Marker(
        location=[the_nearest_5_coffee[0]['latitude'],
                  the_nearest_5_coffee[0]['longitude']],
        icon=folium.Icon(icon="white"),
    ).add_to(m)

    folium.Marker(
        location=[the_nearest_5_coffee[1]['latitude'],
                  the_nearest_5_coffee[1]['longitude']],
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=[the_nearest_5_coffee[2]['latitude'],
                  the_nearest_5_coffee[2]['longitude']],
        icon=folium.Icon(color="red"),
    ).add_to(m)

    folium.Marker(
        location=[the_nearest_5_coffee[3]['latitude'],
                  the_nearest_5_coffee[3]['longitude']],
        icon=folium.Icon(color="black"),
    ).add_to(m)

    folium.Marker(
        location=[the_nearest_5_coffee[4]['latitude'],
                  the_nearest_5_coffee[4]['longitude']],
        icon=folium.Icon(color="pink"),
    ).add_to(m)

    m.save("index.html")


if __name__ == '__main__':
    main()
