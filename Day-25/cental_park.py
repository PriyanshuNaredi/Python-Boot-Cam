import pandas

data = pandas.read_csv("Day-25/Central_Park.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

grey_count = len(grey_squirrels)
red_count = len(red_squirrels)
black_count = len(black_squirrels)

data_dict = {
    "fur_color": ["Grey", "Cinnamon", "Black"],
    "count": [grey_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
