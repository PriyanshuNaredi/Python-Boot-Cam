with open("Day-25/weather_data.csv") as csv_file:
    csv_data = csv_file.readlines()
    print(csv_data)
    
import csv

with open("Day-25/weather_data.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    temperatures = []
    for row in csv_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        
print(temperatures)