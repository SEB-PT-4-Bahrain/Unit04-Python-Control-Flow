print(7!=7)
print(7>7)

print(7>=7)

# and, or
print(True or False)
print(False or False)
print(True and False)
print(True and True)



# ! is the same as not in python

my_name = "Sayed"
print(not my_name == "Youseph")


# if statements

age = 105

if age < 18:
    print("You are too young to drive")
elif age >99:
    print("You are too old sir sorry. no car")
else:
    print("You are good to drive")


my_country = input("Please give your country").lower()
print(f"Wow what a great country {my_country}")

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')


# if color == "green":
#     print("Go")
# elif color == "red":
#     print("stop")
# elif color == "yellow":
#     print("Slow down")
# else:
#     print("Bogus")






# Looping

students = ["Sayed","Youseph","Isra","Malak"]

for student in students:
    print(student)