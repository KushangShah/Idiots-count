if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = int(input())
        students.append([name, score])

    # Featching second lowest grade
    second_lowest_score = None

    for student in students[0][1]:
        if student[1] > second_lowest_score:
            second_lowest_score = student[1]
            break

    # Sorting those idiot
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
    second_lowest_students.sort()

    # printing those idiots out
    for idiot in second_lowest_students:
        print(idiot)
