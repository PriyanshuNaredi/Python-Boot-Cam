import pandas

student_dict = {
    "student": ['Aman', 'Dev', 'Nanu'],
    "score": [56, 76, 98]
}

for (key,value) in student_dict.items():
    print(f"{key} : {value}")
print("-----------------------")
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("-----------------------")
for (key,value) in student_data_frame.items():
    print(f"{key} : {value}")
print("-----------------------")
for (index,row) in student_data_frame.iterrows():
    print(f"{index}:{row}")
print("-----------------------")
for (index,row) in student_data_frame.iterrows():
    print(row.score)
    if row.student == "Nanu":
        print("-----------------------")
        print(row.score)