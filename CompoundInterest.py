P = float(input('The amount of principal originally deposited into the account: $')) #inputs the amount deposited

R = float(input('The annual interest rate paid by the account: %')) #inputs the annual interest

N = float(input('The number of times per year that the interest is compounded: ')) #inputs the number of times per year that the interest is compounded

T = float(input('The number of years the account will be left to earn interest: ')) #inputs the number of years account will be left to earn interest

R /= 100 #rate interest

A = P*((1 + (R/N))**(N*T)) #calculation formula 

print('After ', T, ' years, $', format(A, ',.2f'), ' will be in the account. ', sep='')
