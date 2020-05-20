Course = "Python for Beginners"
print(Course[:])
print(Course[0:5])
print(Course[-1])
print(Course[0])
print(Course[:5])
print(Course[4:])
print(Course[-5])
print(Course[0:-2])

#Formatted String
first_name = 'Miss'
Last_name = 'Swan'
message = '[' + first_name +'] ' + Last_name  + " is a actress"
print(message)
message2 = f'{first_name} [{Last_name}] is a actress'
print(message2)

#String Method
Course = 'Python For Beginners'
print(len(Course))
print(Course.capitalize())
print(Course.casefold())
print(Course.format())
print(Course.isalnum())
print(Course.isascii())
print(Course.isalpha())
print(Course.isdecimal())
print(Course.islower())
print(Course.upper())
print(Course.lower())
print(Course.find('p'))
print(Course.find('o'))
print(Course.find('n'))
print(Course.find('nn'))
print(Course.replace('Beginners','absolute beginners'))
print(Course.replace('P','J'))
print(Course.title())
print("python" in Course)







