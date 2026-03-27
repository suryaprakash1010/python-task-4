def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

# Store multiple users
users = []
users.append(create_user("john doe", 25, "developer"))
users.append(create_user("jane smith", 30, "manager"))

# Print all users
print("User List:")
for user in users:
    print(user)

 #task 2
 
    def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

result = calculate_total(10, 20, 30, 40)
print("\nTotal:", result[0])
print("Average:", result[1])

#task 3
def system_config(**settings):
    print("\nSystem Configuration:")
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")

#task 4
def factorial(n):
    if n < 0:
        return "Error: Negative numbers not allowed"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))
print("Factorial of -3:", factorial(-3))

#task 5
def square_generator(n):
    for i in range(n):
        yield i * i

# Normal list
square_list = [i * i for i in range(5)]
print("\nList:", square_list)
print("Type of list:", type(square_list))

# Generator
gen = square_generator(5)
print("Generator output:", list(gen))
print("Type of generator:", type(square_generator(5)))

#task 6
try:
    num = int(input("\nEnter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")

#task 7
# Write to file
with open("team_data.txt", "w") as file:
    for user in users:
        file.write(f"{user}\n")

# Check if file is closed
print("\nFile closed after writing:", file.closed)

# Read from file
with open("team_data.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)

print("File closed after reading:", file.closed)