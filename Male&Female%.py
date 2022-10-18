males = int(input('Enter the amount of males registered in class: ')) #inputs amount of males   

females = int(input('Enter the amount of females registered in class: ')) #inputs the amount of females


total_of_both = males + females #Adding both males and females to get the total 

males_percentage= males / total_of_both #dividing the males and the total for both males and females to get males percentage

females_percentage = females / total_of_both #dividing the females and the total for both males and females to get females percentage


print('Total number of males: ', format(males_percentage,'.0%')) #Displays the percentage of males
print('Total number of females: ', format(females_percentage, '.0%')) #Displays the percentage of females


