from datetime import datetime
import sys

print("Here you can make notes. Chose what you want in this list. ")
print("1. Add notes.\n" "2. Watch all.\n" "3. Delete all.\n" "4. Exit")
menu = int(input("> "))

if menu == 1:
    note = input("Write your note: \n")
    with open("notes.txt", "a", encoding="utf-8") as notes:
        data = datetime.now().strftime("%Y-%m-%d %H:%M")
        notes.write(f"\n{data}\n{note} \n")
        print("✅ Note saved.")
elif menu == 2:
    with open("notes.txt", "r") as notes:
        print(notes.read())
elif menu == 3:
    with open("notes.txt", "w") as notes:
        pass
elif menu == 4:
    sys.exit()
else:
    print("Select an item from the menu")
    
    
    
from datetime import datetime
import sys
import os

def show_menu():
    print("\n== NOTE MANAGER ===")
    print("1. Add note")
    print("2. Show all notes")
    print("3. Delete all notes")
    print("4. Exit")

notes_file = "notes.txt"

while True:
    show_menu()
    try:
        menu = int(input("> "))
    except ValueError:
        print("Enter a valid number (1-4). ")
        continue