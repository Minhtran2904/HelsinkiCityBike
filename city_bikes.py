def read_file(filename: str):
    with open(filename) as file:
        lines = []
        for line in file:
            line = line.replace('\n', '')
            line = line.strip()
            if 'longitude' in line.lower():
                continue
            lines.append(line)
        return lines

    def get_station_data(filename: str):
    stations_info = read_file(filename)
    stations = {}
    for station in stations_info:
        station_data = station.split(';')
        name = station_data[3]
        long = float(station_data[0])
        lat = float(station_data[1])
        stations[name] = (long, lat)
    return stations

import math
def distance(stations: dict, station1: str, station2: str):
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def longest_distance(stations: dict, stations_list: list, station: str):
    start_index = stations_list.index(station)+1
    compare_list = stations_list[start_index:]
    greatest_tuple = None
    greatest = 0
    for compare in compare_list:
        d = distance(stations, station, compare)
        if d > greatest:
            greatest_tuple = (station, compare, d)
            greatest = d
    return greatest_tuple
