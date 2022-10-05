item1 = float(input('Enter the price for the first item: $'))
item2 = float(input('Enter the price for the second item: $'))
item3 = float(input('Enter the price for the third item: $'))
item4 = float(input('Enter the price for the fourth item: $'))
item5 = float(input('Enter the price for the fifth item: $'))

#all items added 
subtotal = item1 + item2 + item3 + item4 + item5 

#tax
sales_tax = .07

#subtotal is multiplied by sales tax which is .07
total_sales_tax = subtotal * sales_tax

#To get the total, the subtotal of all items is added by result of the subtotal multiplied by the sales tax
total = subtotal + total_sales_tax

print('Your total is = $', total)
#print('\ntotal = $', format(total, ',.2f'))


