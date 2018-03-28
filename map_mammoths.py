import folium
from folium import plugins
import csv


rugby = [48.366629, -99.992145]
zoom = 4

mammoth_map = folium.Map(location=rugby, zoom_start=zoom, tiles='Stamen Terrain')

mammoth_color = {
    "Mammuthus primigenius": "blue",
    "Mammuthus exilis": "purple",
    "Mammuthus columbi": "red",
    "Mammuthus hayi": "yellow",
    "Mammuthus": "orange"
}

lat_lng = []


def escape_quote(string):
    if isinstance(string, str):
        if "'" in string:
            string = str(string).replace("'", "\\'")
    return string


def format_unit(quantity, unit):
    if int(quantity) == 1:
        unit = unit[:-1]
    return unit


def build_marker_text(line_to_parse):
    marker_text_builder = "{} found".format(escape_quote(line_to_parse[0]))
    if line_to_parse[6] or line_to_parse[5] or line_to_parse[7]:
        marker_text_builder += " in"
    if line_to_parse[6]:
        marker_text_builder += " {}".format(escape_quote(line_to_parse[6]))
        if line_to_parse[5] or line_to_parse[7]:
            marker_text_builder += ","
    if line_to_parse[5]:
        marker_text_builder += " {}.".format(escape_quote(line_to_parse[5]))
    if line_to_parse[7]:
        marker_text_builder += "<br>Notes:<br>{}.<br>".format(escape_quote(line_to_parse[7]))

    if line[1]:

        unit = format_unit(escape_quote(line[1]), escape_quote(line[2]))

        marker_text_builder += " {} {} ".format(
            escape_quote(line[1]),
            unit
        )
    return marker_text_builder


with open('mammoth_data.csv') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    first_line = reader.__next__()
    for line in reader:
        lat = line[3]
        lon = line[4]
        marker_text = build_marker_text(line)

        lat_lng.append([lat, lon])
        print(marker_text)

        color = mammoth_color[line[0]]

        marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))
        marker.add_to(mammoth_map)


mammoth_map.save("mammoth_map.html")

heat_map = folium.Map(location=rugby, zoom_start=zoom)
heat_map.add_child(plugins.HeatMap(lat_lng))
heat_map.save("mammoth_heat_map.html")
