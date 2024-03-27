import pandas

data = pandas.read_csv("Day-25/weather_data.csv")
print(type(data))

#
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
print(temp_list)


avg_temp = sum(temp_list)/len(temp_list)
print(data["temp"].mean())

print(data["temp"].max())

# Col Data
print(data["condition"])
print(data.condition)

# Row data

print(data[data.day=="Monday"])
print()
print(data[data.temp == data.temp.max()])

print()

monday = data[data.day=="Monday"]
print(monday.condition)
print("^^^^^^^")
monday_temp = monday.temp
monday_temp_f = monday_temp * 9/5  + 32
print(monday_temp_f)


# CSV file creation 
 
data_dict = {
    "student" : ["A","B","c"],
    "Roll_No" : [1,2,3]
}

Data = pandas.DataFrame(data_dict)

Data.to_csv("Day-25/student_cell.csv")