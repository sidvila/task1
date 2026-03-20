# List containing duplicate values
numbers = [10, 20, 20, 30, 40, 40, 50, 60]

print("Original Data:", numbers)


# Function to remove duplicates
def remove_duplicates(data):
    unique_data = list(set(data))
    return unique_data


# Function to calculate sum of squares
def sum_of_squares(data):
    return sum([x**2 for x in data])


# Lambda function to filter even numbers
filter_even = lambda data: [x for x in data if x % 2 == 0]


# Remove duplicates
clean_data = remove_duplicates(numbers)
print("After Removing Duplicates:", clean_data)

# Filter even numbers
even_numbers = filter_even(clean_data)
print("Filtered Even Numbers:", even_numbers)

# Sum of squares
result = sum_of_squares(even_numbers)
print("Sum of Squares:", result)