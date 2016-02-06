'''
This is a taxes and tip calculator that was written by Chandler Mayo,
in python, for Holberton School. 
'''
print "Welcome to the taxes and tip calculator!" # - Lets welcome the user.
price = input('What is the price before tax? ') # - lets get some user input.
tax = input('What are the taxes? (in %) ') # - lets get some more user input.
tip = input('What do you want to tip? (in %) ') # - lets get even more user input.
price = price * (100 + tax) * (100 + tip) / 10000 # - Math it all up!
print "The price you need to pay is: $%s" % price # - Display the result.