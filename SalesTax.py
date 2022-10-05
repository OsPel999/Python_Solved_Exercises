from os import stat
from turtle import st


purchasetotal = float(input('Enter the amount of your purchase: $'))

state_sales_tax = 0.05
county_sales_tax = 0.025

state_tax = purchasetotal * state_sales_tax

county_tax = purchasetotal * county_sales_tax

total_sales_tax = state_sales_tax + county_sales_tax

total = purchasetotal + total_sales_tax

print('Amount of your purchase: $', purchasetotal)
print('State sales tax: $', state_tax)
print('County sales tax: $', county_tax)
print('Total sales tax', total_sales_tax)
print('Your total is: $', total)

