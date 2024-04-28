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

def calculate_weighted_average(numbers, weights):
  
    if not numbers or not weights:
        raise TypeError("Both lists cannot be empty.")

    if len(numbers) != len(weights):
        raise ValueError("Lists of numbers and weights must have the same length.")

    if not all(isinstance(num, (int, float)) for num in numbers) \
            or not all(isinstance(weight, (int, float)) for weight in weights):
        raise TypeError("Both lists can only contain numbers.")

    weighted_sum = sum(weight * num for weight, num in zip(weights, numbers))
    total_weight = sum(weights)
    weighted_average = weighted_sum / total_weight
    return weighted_average


numbers = [10, 20, 30, 40, 50]
weights = [0.2, 0.3, 0.4, 0.2, 0.1]

weighted_average = calculate_weighted_average(numbers, weights)
print("Weighted Average:", weighted_average) 