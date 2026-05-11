while True:
    print("\n" + "=" * 40)
    print(" PATTERN PROGRAMS")
    print("=" * 40)
    print("1. Star Triangle")
    print("2. Reverse Star Triangle")
    print("3. Number Triangle")
    print("4. Reverse Number Triangle")
    print("5. Pyramid")
    print("6. Inverted Pyramid")
    print("7. Diamond")
    print("8. Floyd's Triangle")
    print("9. Alphabet Triangle")
    print("10. Exit")
    print("=" * 40)
   
    choice = int(input("enter choice: "))
   
    if choice == 10:
        break
    elif choice == 1:
        print("\nSTAR TRIANGLE")
        row = int(input("Enter your number: "))
        for i in range(1, row + 1):
            for j in range(i):
                print("*", end="")
            print()
           
    elif choice == 2:
        print("\nREVERSE STAR TRIANGLE")
        row = int(input("Enter your number: "))
        for i in range(row, 0, -1):
            for j in range(i):
                print("*", end="")
            print()
       
    elif choice == 3:
        print("\nNUMBER TRIANGLE")
        row = int(input("Enter your number: "))
        for i in range(1, row + 1):
            for j in range(i):
                print(j + 1, end="")
            print()
           
    elif choice == 4:
        print("\nREVERSE NUMBER TRIANGLE")
        row = int(input("Enter your number: "))
        for i in range(row, 0, -1):
            for j in range(i):
                print(j + 1, end="")
            print()
           
    elif choice == 5:
        print("\nPYRAMID")
        row = int(input("Enter your number: "))
        for i in range(1, row + 1):
            spaces = row - i
            stars = 2 * i - 1
            for j in range(spaces):
                print(" ", end="")
            for k in range(stars):
                print("*", end="")
            print()
           
    elif choice == 6:
        print("\nINVERTED PYRAMID")
        row = int(input("Enter your number: "))
        for i in range(row, 0, -1):
            spaces = row - i
            stars = 2 * i - 1
            for j in range(spaces):
                print(" ", end="")
            for k in range(stars):
                print("*", end="")
            print()
    elif choice == 7:
        print("\nDIAMOND")
        row = int(input("Enter your number: "))
        # Normal Pyramid
        for i in range(1, row + 1):
            spaces = row - i
            stars = 2 * i - 1
            for j in range(spaces):
                print(" ", end="")
            for k in range(stars):
                print("*", end="")
            print()
        # Inverted Pyramid
        for i in range(row - 1, 0, -1):
            spaces = row - i
            stars = 2 * i - 1
            for j in range(spaces):
                print(" ", end="")
            for k in range(stars):
                print("*", end="")
            print()
    elif choice == 8:
        print("\nFLOYD's TRIANGLE")
        row = int(input("Enter your number: "))
        num = 1
        for i in range(1, row + 1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()
    elif choice == 9:
        print("\nALPHABET TRIANGLE")
        row = int(input("Enter your number: "))
        for i in range(1, row + 1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()
            
    else:
    	print("Invalid Choice")
