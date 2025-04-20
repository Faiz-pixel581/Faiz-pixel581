print("Welcome to the tip calculator!\n") # Greeting

# Getting user input and converting to correct types using string and placing the answers in respective containers, i.e variables.
Bill = float(input("What was the total bill?\n"))
Tip = float(input("How much tip would you like to give: 10%, 12%, or 15%?\n"))
Split = int(input("How many people should split the bill?\n"))

# Calculating the total amount each person should pay
tip_amount = Bill * (Tip / 100) # The Formula
total_bill = Bill + tip_amount # 2nd Step
amount_per_person = total_bill / Split

# Rounding the result to 2 decimal places using 'round()' function.
amount_per_person = round(amount_per_person, 2)

# Printing the result Day Day 2
print(f"Each person should pay: ${amount_per_person}")