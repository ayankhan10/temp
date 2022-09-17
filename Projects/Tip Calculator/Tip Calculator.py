# Tip Calculator
# Level : Easy
# Date: May 4, 2022

# Input

bill_ammount = float(input("Enter the bill ammount: ")) 
number_of_people =int(input("Enter the number of people: "))
tip_percent = float(input("Enter the percentage of bill you would like to tip: ")) 

# Calculations
total_ammount = bill_ammount + ((tip_percent/100) * bill_ammount)
indi_payment = total_ammount/ number_of_people

# Outputs
print(f"Your total bill with tip is {total_ammount}.")
print(f"Ecah person has to pay $ {indi_payment}.")