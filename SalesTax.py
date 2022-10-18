purchasetotal = float(input('Enter the amount of your purchase: $')) #inputs amount of purchase

state_sales_tax = 0.05 #represents the state sales tax
county_sales_tax = 0.025 #represents the county sales tax

state_tax = purchasetotal * state_sales_tax #calculates the state tax by multiplying the purchasetotal and state sales tax

county_tax = purchasetotal * county_sales_tax #calculates the county tax by multiplying the purchasetotal and county sales tax

total_sales_tax = state_sales_tax + county_sales_tax #calculates the total sales tax by adding the county sales tax and state sales tax

total = purchasetotal + total_sales_tax #calculates the total by adding the purchase total and total sales tax

#Displays the calculations
print('Amount of your purchase: $', purchasetotal)
print('State sales tax: $', state_tax)
print('County sales tax: $', county_tax)
print('Total sales tax', total_sales_tax)
print('Your total is: $', total)

