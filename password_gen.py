# Osman Manaf python project

# Adding the import function to my python script 
import random

#Initialization  of variables 

Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower_case = "abcdefghijklmnopqrstuvwxyz"
Numbers = "123456789"
Symbols = "<>?*&^#@!%+$£./():;"

# assigning of variables upper_case,lower_case,Number and symbol to Results 

Results = Upper_case + Lower_case + Symbols + Numbers 

length = 12

# code assigns string input from users password to generate random password 

Password = "" . join(random.sample(Results,length))

print ("please your new created password is " , Password)
