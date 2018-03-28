import folium
import os


map_mn = folium.Map(location=[45, -93.2], zoom_start=13)

folium_marker = folium.Marker([44.9729, -93.2831]).add_to(map_mn)


rugby = [48.366629, -99.992145]

us_map = folium.Map(location=rugby, zoom_start=4)

#folium_marker = folium.Marker([44.9729, -93.2831]).add_to(map_mn)


map_mn.save('mn_map.html')

us_map.save('us_map.html')
