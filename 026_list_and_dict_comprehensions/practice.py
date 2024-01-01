numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print([n**2 for n in numbers])

numbers = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]

print([n for n in numbers if not n%2])

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
student_scores = {name:random.randint(0,100) for name in names}

#print(student_scores.items())
print({name:score for (name, score) in student_scores.items() if student_scores[name] >= 60})
