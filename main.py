while True:
    print("1.Add\n 2.Minus\n 3.Multiply\n 4.Divede\n 5.Exit")
    
    try:
        menu = int(input("Chose number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if menu == 5:
        print("You have exited in your program")
        break
    
    print("Input two numbers")
    first = int(input("Input first number: "))
    second = int(input("Input second number: "))
    print(first, second)
    
    if menu == 1:
        output = first + second
    elif menu == 2:
        output = first - second
    elif menu == 3:
        output = first * second
    elif menu == 4:
        output = first / second
    else:
        print("Select an item from the menu")
        
    print("It`s your numbers: ", output)