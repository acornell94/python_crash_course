students_present = {
    'frank': 'freshman',
    'thomas': 'freshman',
    'sam': 'junior',
    'justin': 'senior',
    'shawn': 'sophomore',
}

expected_students = ['joe', 'thomas', 'barbara', 'sam', 'frank', 'shawn', 'justin', 'brandon']

for student in expected_students:
    if student in students_present.keys():
        print(student.title() + ", thank you for joining us today.")
    else:
        print("Has anyone seen " + student.title() + "?")