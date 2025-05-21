#lower 18 do not entry !!!
while True :
    
    name = str(input("Enter your name : "))
    print("Enter Your birth")
    day,month,year= int(input("Day : ")) , input("Month : ") , int(input("Years: "))
    if year <= 2025 :
        break
    elif year > 2025 :
        print("ERROR!")

print(f"Your birth day is : {day} {month} {year}")

if 2025 - year >= 20 :
    print(f"Welcome {name} ")
elif 2025 - year < 20 :
    print(f"{name} not allowed to enter.")    
else :
    print("error")
        