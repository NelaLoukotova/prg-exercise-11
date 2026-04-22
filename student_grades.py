class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, value):
        result = []

        for i in range(len(self.scores)):
            if self.scores[i] == value:
                result.append(i)
        return result

    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)

        for j in range(n):
            swapped = False
            for i in range(0, n - j - 1):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
                    swapped = True
            if not swapped:
                break

        return scores

if __name__ == "__main__":
     results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

     print(results.count())  # 9
     print(results.get_by_index(2))  # 91
     print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

     print(results.get_grade(2))  # A (91 bodů)
     print(results.get_grade(6))  # A (100 bodů)
     print(results.get_grade(7))  # F (38 bodů)

     print(results.find(100))  # [6]
     print(results.find(50))  # [4]
     print(results.find(77))  # []

     print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
     print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny


