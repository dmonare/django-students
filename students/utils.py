import random

def get_random_students():
    names = ['Nika', 'Zangi', 'Dito', 'Jemali', 'Levani']
    surnames = ['narmania', 'zangishvili', 'beglarishvili', 'Bakhia', 'kobaxidze']
    
    students = []
    for _ in range(100):
        student = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    
    return students
