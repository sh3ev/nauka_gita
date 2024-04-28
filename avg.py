def calculate_average(numbers):

    if not numbers:
        raise TypeError("List cannot be empty.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List can only contain numbers.")

    total = sum(numbers)
    average = total / len(numbers)
    return average


numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average) 