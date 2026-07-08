print("-----Age Category Checker-----")

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age. Age cannot be negative.")
elif age > 130:
    print("Invalid age. Age cannot be greater than 130.")
else:
    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")