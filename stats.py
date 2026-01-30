# writing a python script to calculate the average of a list of numbers

def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(average(numbers))

# writing a python script to calculate the median of a list of numbers

def median(numbers):
    return sorted(numbers)[len(numbers) // 2]

numbers = [1, 2, 3, 4, 5]
print(median(numbers))

# writing a python script to calculate the mode of a list of numbers

def mode(numbers):
    return max(set(numbers), key=numbers.count)

numbers = [1, 2, 3, 4, 5]
print(mode(numbers))
