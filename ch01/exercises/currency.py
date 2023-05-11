
amount = input("Enter the amount: ")
amount = float(amount)
rate = input("Enter the exchange rate: ")
rate = float(rate)
new_amount = amount*rate
minus_fees = new_amount - 3
print("Your result minus a $3 exchange rate is: ", minus_fees)
