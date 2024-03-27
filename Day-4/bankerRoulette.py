import random
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

size = len(names)

random = random.randint(0,size-1)

print(f"{names[random]} is going to buy the meal today!")

