#1
print("=== Membership Application ===")
a = input("Please enter the first name of the applicant:")
b = input("Last name:")
c,d,e = input("Your birthday(year month date):").split()
x = int(c)
age = 2024 - x
f = input("Your blessing:")
print(age)


print('')
print(f'Welcome {b}, {a} ({c} / {d} / {e} , age {age})')
print(f)
