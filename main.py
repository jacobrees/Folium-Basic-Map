import folium

map = folium.Map(location=[51.5, -0.1], zoom_start=6)
map.add_child(folium.Marker(location=[51.622846, -3.941989], popup="shitty city", icon=folium.Icon(color="green")))
map.save("Map1.html")