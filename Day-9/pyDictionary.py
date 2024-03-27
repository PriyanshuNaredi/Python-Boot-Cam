programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary["Bug"])

#Add new Entry
programming_dictionary["Loop"] = "......."
print(programming_dictionary)

#Empty Dic
empty_dictionary = {}

#delete existing
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Loop"] = "Do something again & again"

# Dictionary Traversal
for i in programming_dictionary:
    print(i)
    print( programming_dictionary[i])
    empty_dictionary[i] = programming_dictionary[i]

