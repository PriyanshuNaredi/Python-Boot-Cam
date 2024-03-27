# try:
#     file = open("Day-30/a.txt")
# except FileNotFoundError:
#     print("error occurred")
#     file = open("Day-30/a.txt","w")
# else:
#     cont = file.read()
#     print(cont)
# finally:
#     file.close()
#     print("Bye")
    
    
    
h = float(input("h: "))
w = float(input("W: "))
if h>3:
    raise ValueError("Human height should not be over 3 m.")
bmi = w/h ** 2
print(bmi)
