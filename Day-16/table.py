from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.border = False
table.add_column("Pokemon",["Pikachu ","Ledian "])
table.add_column("Type",["Electric ","Fire "])

print(table)

