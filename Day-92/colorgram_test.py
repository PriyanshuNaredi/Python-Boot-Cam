import collections
import colorgram


rgb_colors = []
hex_colors = []
colors = colorgram.extract('Day-92/sample.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    hex_color = '#%02x%02x%02x' % (new_color)
    hex_colors.append(hex_color)
    rgb_colors.append(new_color)

print(hex_colors)
# print(rgb_colors)

print(collections.Counter(hex_colors).most_common()[0])