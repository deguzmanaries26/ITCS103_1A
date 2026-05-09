import openpyxl as grande
import os 

wb = grande.Workbook()
ws = wb.active
ws.append(["ID","First Name","Last Name","Birth Date","Age"])
records = []
for ariana in range (1,4):
    print(f"\nFavorite Person {ariana}")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    bYear = input("Birth Year: ")
    if not bYear.isdigit():
        print("Birth Years must be number")
        print("\nInput not saved\n")
        print("Run the system again\n")
        print("Thank you!\n")
        exit()
    
    newb = int(bYear)
    age = 2026 - newb
    records.append([f"0{ariana}", fName, lName, newb, age])
    ws.append([f"0{ariana}", fName, lName, newb, age])
wb.save("favorite_people.xlsx")
os.system("cls")


print("\nFavorite People saved successfully!\n")
print("----- FAVORITE PEOPLE LIST -----")
for record in records:
    print(record)

ask = input("\nPlease press ENTER to exit...")
if ask == "":
    os.system("cls")
else:
    print("Invalid input. Exiting the program.")
print("\n----- thank u, next -----\n")

