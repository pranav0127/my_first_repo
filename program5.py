#if statements

"""it's hot
its a hot day
drink plenty of water
otherwise if its cold
it a cold day
otherwise
its a lovely day
"""

is_hot = False
is_cold = False
if is_hot:
    print("its a hot day")
    print("drink plenty of water")

elif is_cold:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
print("Enjoy your day")



"""Price of a house is 1 million dollar
if buyer has good credit they need to put down 10%
otherwise they need to down payment 20% 
print the down payment """

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"the down payment is {down_payment}$")


#if the applicant has high income and good credit then ony eligible for loan
high_income = True
good_credit = True
if high_income and good_credit:
    print("eligible for loan")

high_income = False
good_credit = False
if high_income or good_credit:
    print("eligible for loan")
else:
    print("please get outside from bank")

high_income = True
criminal_data = True
if high_income and not criminal_data:
    print("eligible for loan")
else:
    print("you are criminal")


#Comparison operator
"""if temperature is 30
its a hot day
if temperature is less than 10
its a winter day
otherwise
its neither cold nor hot
"""
temp = 30
if temp > 30:
    print("its a hot day")
elif temp < 10:
    print("its a cold day")
else:
    print("neither hot nor cold")

"""if name is less than 3 character long then 
name must be at least 3 character
otherwise if its more than 50 characters long then 
name cant be taken or valid please check"""

name = "John smith"
if len(name)<3:
    print("name should be of more than 3 character")
elif len(name)>50:
    print("name not be valid")
else:
    print("sounds good")

#project
#weight converter

weight = int(input("weight: "))
unit = input("in (K)grams or (L)bs: ")
if unit.upper() == "l":
    converter = weight / 0.45
    print(f"the weight of yours choice is {converter}lbs")
else:
    converter = weight * 0.45
    print(f"the weight of yours choice is {converter}kilos")






