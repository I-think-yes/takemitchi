try:
    f = open("mikey.txt" , "x")
    f.write("shopping list manager")
    f.close()
except fileExistsError: 
    print("ERROR")

items = []

while True:
    print("\nMENU")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Show")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        new_item = input("Enter item to add: ")
        items.append(new_item)
        print("Item added!")

