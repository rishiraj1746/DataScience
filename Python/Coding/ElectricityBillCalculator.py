print("-----Electricity Bill Calculator-----")

units_consumed = float(input("Enter the number of units consumed: "))
if 0 < units_consumed <= 100:
    bill_amount = units_consumed * 5
    print(f"The electricity bill amount is: Rs. {bill_amount}")
elif 100 < units_consumed <= 200:
    bill_amount = (100 * 5) + ((units_consumed - 100) * 7)
    print(f"The electricity bill amount is: Rs. {bill_amount}")
elif 200 < units_consumed:
    bill_amount = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)
    print(f"The electricity bill amount is: Rs. {bill_amount}")
else:
    print("Invalid input. Please enter a positive number of units consumed.")

bill_amount = round(bill_amount, 2)
print(f"The electricity bill amount is: Rs. {bill_amount}")
