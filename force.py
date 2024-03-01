print("newton's second law of moton ")
print("----------------------------------")
# determine the missng value
print ("select the missing value:")
print("1. mass (m)")
print ("2. acceleration (a)")
print ("3. force (f)")
missing_value_choice =input("enter the option nujmber for missing value")
#prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("enter acceleration (a): "))
    F = float(input("enter force (F):"))
    m = F / a
    print(f"mass (m) = {m}")
elif missing_value_choice == "2":
    m = float(input("enter mass (m): "))
    a = F / m 
    print(f"Acceleration (a) = {a}")
elif missing_value_choice == "3":
    m = float(input("Enter mass (m):"))
    a = float(input("Enter acceleration (a): "))
    F = m * a
    print(f"force (F) = {F}")
else:
    print("invalid option selected for the missing value.")


