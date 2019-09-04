# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

age = input("Input a dog's age in human years: ")
age= int(age)
new_age=0

for num in range(age):
    if num == 0:
        new_age+=10
    elif num == 1:
        new_age+=10
    else:
        new_age+=7    
    
    
print(f"The dog's age in dog years is {new_age}")

