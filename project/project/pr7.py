import datetime
import time
import math
import random
import uuid
import importlib
from mytoolkit import file_ops, math_utils

def show_menu():
    print("\n" + "="*30)
    print("Welcome to Multi-Utility Toolkit")
    print("="*30)
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("="*30)

def handle_datetime():
    print("\n1. Display current date/time\n2. Calculate date difference")
    choice = input("Choice: ")
    if choice == '1':
        print(f"Current: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    elif choice == '2':
        d1 = input("Enter first date (YYYY-MM-DD): ")
        d2 = input("Enter second date (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        print(f"Difference: {abs((date2 - date1).days)} days")

def handle_math():
    print("\n1. Factorial\n2. Compound Interest\n3. Area of Circle")
    choice = input("Choice: ")
    if choice == '1':
        num = int(input("Enter number: "))
        print(f"Factorial: {math.factorial(num)}")
    elif choice == '2':
        p = float(input("Principal: "))
        r = float(input("Rate: "))
        t = float(input("Time: "))
        print(f"Compound Interest: {math_utils.compound_interest(p, r, t):.2f}")

def handle_random():
    print("\n1. Random Number\n2. Generate Password")
    choice = input("Choice: ")
    if choice == '2':
        length = int(input("Length: "))
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        pwd = "".join(random.sample(chars, length))
        print(f"Generated Password: {pwd}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1': handle_datetime()
        elif choice == '2': handle_math()
        elif choice == '3': handle_random()
        elif choice == '4': print(f"Generated UUID: {uuid.uuid4()}")
        elif choice == '5':
            fname = input("Enter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_to_file(fname, data)
            print(f"File Content: {file_ops.read_from_file(fname)}")
        elif choice == '6':
            mod_name = input("Enter module name (e.g., math, random): ")
            try:
                mod = importlib.import_module(mod_name)
                print(f"Attributes: {dir(mod)[:10]}...")
            except:
                print("Module not found.")
        elif choice == '7':
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

if __name__ == "__main__":
    main()
