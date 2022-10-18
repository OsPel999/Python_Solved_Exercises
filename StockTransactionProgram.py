stockbroker_commission = .03 #commission rate

shares_sold = shares_purchased = 2000 #shares sold

price_per_share = 40 #price per share amount


amount_paid_for_stock = shares_purchased * price_per_share #calculates the amount paid for stock by multiplying shares purchased by price per share

print(amount_paid_for_stock) #displays the amount paid for stock


commission_paid_when_purchased = amount_paid_for_stock * stockbroker_commission #calculates the commission paid when purchased by multiplying amount paid for stock by stock broker commission

print(commission_paid_when_purchased) #displays the commission paid when purchased 


price_per_share = 42.75 #price per share amount

amount_stock_sold = shares_sold * price_per_share #calculates amount stock sold by multiplying shares sold by price per share
print(amount_paid_for_stock)#displays the amount paid for stock

commission_paid_when_sold = amount_paid_for_stock * stockbroker_commission #calculates commission paid when sold by amount paid for stock bt stockbroker commission
print(commission_paid_when_sold) #displays the commission paid when sold

amount_remaining = amount_paid_for_stock - (commission_paid_when_purchased + commission_paid_when_sold) #calculates the amount remaining by subtracting amount paid for stock
                                                                                                        #by commission paid when purchased plus commission paid when sold

print(amount_remaining) #displays the amount remaining
