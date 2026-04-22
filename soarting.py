import matplotlib.pyplot as plt
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    for j in range(len(values)):
        min_index = j
        min_values = values[min_index]
        for i in range(j + 1, len(values)):
            if values[i] < min_values:
                min_index = i
                min_values = values[i]
        print(values)
        values[j], values[min_index] = values[min_index], values[j]
        print(values)
    return values
def bubble_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)
    plt.ion()
    plt.show()
    for j in range(n):
        swapped = False
        for i in range(0, n - j - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

    plt.ioff()
    plt.show()
    return numbers


if __name__ == '__main__':


    values = random_numbers(20)
    print(values)
    print(bubble_sort(values))



