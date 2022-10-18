one_acre = 43,560 #represents amount of acres

total_SQFT = int(input('Enter the total square feet: ')) #inputs the total square feet

number_of_acres = sum(one_acre) / total_SQFT #calculation formula

print(format(number_of_acres,'.2f')) #Displays the number of acres