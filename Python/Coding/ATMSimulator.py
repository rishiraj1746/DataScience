print("-----ATM Simulator-----")

balance = float(input("Enter your current balance: "))

action = input("Choose an action (withdraw or deposit): ").lower()
if action == "withdraw":
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.") 
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance}")
elif action == "deposit":
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit successful. New balance: {balance}")
else:
    print("Invalid action.")
