length_of_row_ft = float(input('Enter the length of the row in feet: ')) #inputs length of the row in feet 

amount_of_space = float(input('Enter the amount of space used by end-post assembly in feet: ')) #inputs the amount of space used by end-post assembly in feet

amount_of_space_bwt_vines = float(input('Enter amount of space between the vines, in feet: ')) #inputs amount of space between the vines in feet

number_of_grapevines = (length_of_row_ft - (2 * amount_of_space)) / amount_of_space_bwt_vines #formula 

print('The number of grapevines that will fit in the row is: ', number_of_grapevines) #displays the number of grapevines that will fit in the row