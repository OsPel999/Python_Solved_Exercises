foodcharge = float(input('Enter the amount charged for the food: $'))

tip_percentage = .18
SALES_TAX = .07

tip = foodcharge * tip_percentage
sales_tax = foodcharge * SALES_TAX

total = foodcharge + tip + sales_tax
print('Amount you spent on food: $ ', foodcharge)
print('Tip: $', tip)
print('Sales Tax: $', format(sales_tax, ',.2f'), sep='')
print('Your complete total is: $', total)