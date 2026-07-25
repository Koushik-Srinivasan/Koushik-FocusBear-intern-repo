# Task 2: Simple Math

# Step 1: ask the user for the first number
first_number_text = input("Enter the first number: ")

# Step 2: ask the user for the second number
second_number_text = input("Enter the second number: ")

# Step 3: convert the text input into actual numbers
first_number = float(first_number_text)
second_number = float(second_number_text)

# Step 4: do the maths
total_sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number

# Step 5: print the results one at a time
print("Sum: " + str(total_sum))
print("Difference: " + str(difference))
print("Product: " + str(product))

# Step 6: handle division carefully, in case the second number is 0
if second_number != 0:
    quotient = first_number / second_number
    print("Quotient: " + str(quotient))
else:
    print("Quotient: cannot divide by zero")
