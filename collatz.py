while True:
    steps = 0
    #1
    c0 = int(input("Enter number: "))
    if c0 <= 0:
        break
    while c0 != 1:
        steps += 1
        #2
        if c0 % 2 == 0:
            c0 = c0 / 2
    #3
        else:
            c0 = 3 * c0 + 1
    #4
        if c0 == 1:
            print(int(c0))
            break
        else:
            print(int(c0))
    print(f"Steps: {steps}")

