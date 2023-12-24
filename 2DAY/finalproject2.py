print("welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?" ))
tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person , 2)
print(f"the amount each person has to pay {final_amount}")

