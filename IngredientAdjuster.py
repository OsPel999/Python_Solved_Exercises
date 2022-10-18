NumberofCookies = float(input('Enter the amount of cookies you want to bake: ')) #inputs the amount of cookies desired to bake

cookies = 48 #represents the amount of cookies
sugar = 1.5 #amount of sugar needed to bake cookies
butter = 1 #amount of butter needed to bake cookies
flour = 2.75 #amount of flour needed to bake cookies

Sugar_total = (sugar * NumberofCookies) / cookies #calculates the total amount of sugar by multiplying sugar amount by the number of cookies desired to bake divided by the cookie amount
butter_total = (butter * NumberofCookies) / cookies #calculates the total amount of butter needed by multiplying butter amount by the number of cookies desired to bake divided by the cookie amount
flour_total = (flour * NumberofCookies) / cookies #calculates the total amount of flour needed by multiplying flour amount by the number of cookies desired to bake divided by the cookie amount

print(NumberofCookies) #Displays the amount of cookies desired to bake
print('Cups of sugar: ', Sugar_total) #Displays amount of sugar needed to bake cookies
print('Cups of butter: ', butter_total) #Displays amount of butter needed to bake cookies
print('Cups of flour: ', flour_total) #Displays amount of flour needed to bake cookies