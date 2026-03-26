# Employee Management System
employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    employees.append({"name": name, "age": age, "role": role, "salary": salary})

def display_employees():
    for emp in employees:
        print(emp)

def update_employee(name):
    for emp in employees:
        if emp["name"] == name:
            emp["role"] = input("New role: ")
            emp["salary"] = float(input("New salary: "))

def delete_employee(name):
    global employees
    employees = [emp for emp in employees if emp["name"] != name]

    
# Student Report Card

def report_card():
    name = input("Enter student name: ")
    m1 = int(input("Mark1: "))
    m2 = int(input("Mark2: "))
    m3 = int(input("Mark3: "))
    
    total = m1 + m2 + m3
    avg = total / 3
    
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print(f"\nReport Card\nName: {name}\nTotal: {total}\nAverage: {avg:.2f}\nGrade: {grade}")

    # Shopping Cart System
    cart = []

def add_item():
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    
    cart.append({"name": name, "price": price, "qty": qty})

def total_bill():
    total = sum(item["price"] * item["qty"] for item in cart)
    print("Total Bill:", total)

def remove_item(name):
    global cart
    cart = [item for item in cart if item["name"] != name]

def display_cart():
    for item in cart:
        print(item)

# Login System
users = {"admin": "1234", "user": "abcd"}

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    if username in users and users[username] == password:
        print("Login Successful")
    else:
        print("Invalid Credentials")

# Unique Visitor Counter
visitors = set()

def add_visitor():
    name = input("Visitor name: ")
    visitors.add(name)

def show_visitors():
    print("Unique visitors:", len(visitors))

# String Formatter Tool
def formatter():
    name = input("Enter name: ")
    product = input("Enter product: ")
    
    print(f"{name} purchased {product}")
    print(name.ljust(20, "-"))
    print(name.rjust(20, "-"))
    print(name.center(20, "-"))

# Bank Account System
account = {"name": "", "balance": 0}

def create_account():
    account["name"] = input("Enter name: ")
    account["balance"] = float(input("Initial balance: "))

def deposit():
    amt = float(input("Amount to deposit: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Amount to withdraw: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

def check_balance():
    print("Balance:", account["balance"])


# Voting System
votes = {"A": 0, "B": 0, "C": 0}

def vote():
    choice = input("Vote (A/B/C): ")
    if choice in votes:
        votes[choice] += 1

def winner():
    print("Winner:", max(votes, key=votes.get))

# Course Enrollment System
students = {}

def add_student():
    name = input("Student name: ")
    courses = input("Courses (comma separated): ").split(",")
    students[name] = courses

def update_courses(name):
    if name in students:
        students[name] = input("New courses: ").split(",")

def display_students():
    for name, courses in students.items():
        print(name, ":", courses)

# Number Utility Tool

def number_tool():
    num = int(input("Enter number: "))
    
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hex:", hex(num))
    
    print("Formatted:", f"{num:,}")
    print("Scientific:", f"{num:.2e}")