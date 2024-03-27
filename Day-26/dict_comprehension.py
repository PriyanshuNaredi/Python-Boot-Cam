import random

names = ['Aman', 'Dev', 'Nanu']

student_score = {student: random.randint(50, 100) for student in names}

passed_students = {student: score for (student, score) in student_score.items() if score > 65}
