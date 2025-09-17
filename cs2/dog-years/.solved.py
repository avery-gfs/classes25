# Get two numbers as input from the user: their birth year, and
# their dog's birth year. Calculate and print the user's age in
# years, the dog's age in years, and the dog's age in dog-years.

birthYear = int(input("Enter your birth year: "))
dogBirthYear = int(input("Enter your dog's birth year: "))

age = 2025 - birthYear
dogAge = 2025 - dogBirthYear

print(f"Your age (years): {age}")
print(f"Your dog's age (years): {dogAge}")
print(f"Your dog's age (dog-years): {dogAge * 7}")

# Challenge: calculate your approximate age in months, days, hours,
# minutes, and seconds
