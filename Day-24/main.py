file = open("Day-24\my.txt")
contents = file.read()
print(contents)
file.close()

with open("Day-24\my.txt") as file:
    contents = file.read()
    print(contents)
    
with open("Day-24\my.txt",mode="a") as file:
    file.write("\nNew text")
    
        
with open("Day-24\ New_file.txt",mode="w") as file:
    file.write("\nNew @-@ text")