# Task 3: Your Age in Dog Years

# Step 1: ask the user for their age
age_text = input("Enter your age: ")

# Step 2: convert the text into a whole number
age = int(age_text)

# Step 3: calculate dog years (1 human year = 7 dog years)
dog_years = age * 7

# Step 4: print the result
print("You are " + str(age) + " human years old.")
print("That is " + str(dog_years) + " in dog years!")
