NumberofCookies = float(input('Enter the amount of cookies you want to bake: '))

cookies = 48
sugar = 1.5
butter = 1
flour = 2.75

Sugar_total = (sugar * NumberofCookies) / cookies
butter_total = (butter * NumberofCookies) / cookies
flour_total = (flour * NumberofCookies) / cookies

print(NumberofCookies)
print('Cups of sugar: ', Sugar_total)
print('Cups of butter: ', butter_total)
print('Cups of flour: ', flour_total)