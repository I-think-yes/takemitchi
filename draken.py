try:
    f = open("mikey.txt" , "x")
    f.write("shopping list manager")
    f.close()
except FileExitsError:
    print("ERROR")