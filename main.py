from soarting import random_numbers
from student_grades import StudentsGrades
if __name__ == "__main__":

    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])


    print("Počet studentů:", results.count())


    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")


    print("Studenti se 100 body:", results.find(100))


    print("Seřazené výsledky:", results.get_sorted())




    random_results = StudentsGrades(random_numbers(30, 0, 100))

    print("Počet studentů:", random_results.count())
    print("Seřazené výsledky:", random_results.get_sorted())