import random

def generate_random_numbers(count=10, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]
 def calculate_average(numbers):
    return sum(numbers) / len(numbers)
 print("Generated random numbers:")
 print("Average:", calculate_average(generate_random_numbers(10))))