num_char = len(input("what is your name?\n"))

print(type(num_char))

# Type casting

int_char = str(num_char)

print("Your name has " + int_char + " charecters.")

a = 70 + 100.5
b = 70 + float("100.5")
print( type(a) )
print( type(b) )
