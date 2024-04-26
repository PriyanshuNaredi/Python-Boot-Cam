from colorthief import ColorThief

color_thief = ColorThief('Day-92/sample.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=10)

print(palette)


hex_colors = []

for i in palette:
    hex_color = '#%02x%02x%02x' % (i)
    hex_colors.append(hex_color)
    
print(hex_colors)