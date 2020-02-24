



'''
This is a python program to get user input and output the data
'''

#Get user input

fav_intnumber = int(input("Enter your favourite whole number: "))
fav_fruit = input("Enter your favourite fruit: ")
fav_decnum = float(input("Enter your favourite decimal number: "))
fav_bool = input("Enter any boolean value: ")

data = (fav_intnumber, fav_decnum, fav_fruit)
format= "Your favourite integer is %d \n Your favourite decimal number is %f \n Your favorite fruit is:\033[1m %s "
print (format % data)
