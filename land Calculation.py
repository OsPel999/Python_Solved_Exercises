one_acre = 43,560

total_SQFT = int(input('Enter the total square feet: '))

number_of_acres = sum(one_acre) / total_SQFT

print(format(number_of_acres,'.2f'))