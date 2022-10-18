foodcharge = float(input('Enter the amount charged for the food: $')) #inputs the amount charged

tip_percentage = .18 #tip percentage amount
SALES_TAX = .07 #sales tax amount

tip = foodcharge * tip_percentage #calculates the tip by multiplying foodcharge by tip percentage
sales_tax = foodcharge * SALES_TAX #calculates the sales tax by multiplying foodcharge by sales tax

total = foodcharge + tip + sales_tax #calculates the total by adding the foodcharge, tip and sales tax

#displays the foodcharge, tip, sales tax and total in order
print('Amount you spent on food: $ ', foodcharge)
print('Tip: $', tip)
print('Sales Tax: $', format(sales_tax, ',.2f'), sep='')
print('Your complete total is: $', total)