# 💰 Tip Calculator

A beginner-friendly Python script that calculates how much each person should pay when splitting a bill, including a customizable tip percentage.

## 📌 Features
- Takes user input for:
  - Total bill amount
  - Tip percentage (10%, 12%, or 15%)
  - Number of people sharing the bill
- Calculates the total amount per person
- Rounds the result to two decimal places for currency formatting

## 🧮 Formula Used

```python
tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
amount_per_person = total_bill / split
🛠️ Technologies
Python 3

🔄 How to Run
Simply run the script in a Python environment:

bash
Copy
Edit
python tip_calculator.py
✅ Example Output
pgsql
Copy
Edit
Welcome to the tip calculator!

What was the total bill?
> 100

How much tip would you like to give: 10%, 12%, or 15%?
> 12

How many people should split the bill?
> 3

Each person should pay: $37.33
📫 Connect with me on my Email - mf073027@gmail.com.
