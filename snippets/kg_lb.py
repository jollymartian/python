while True:    

    weight_loop = True
    l_or_k_loop = True
    
    while weight_loop == True:
        weight = float(input("Enter weight: "))
        print(type(weight))
        if type(weight) != float:
            print("Not a number, try again!")
            continue
        else:
            weight_loop = False
    
    while l_or_k_loop == True:
        l_or_k = input("(K)g's or (L)b's: ")
        l_or_k = l_or_k.lower()
        print(l_or_k)
        if l_or_k == "k" or "l":
            l_or_k_loop = False
        else:
            print("Not 'k' or 'l', try again!")
            continue
    break
   
if l_or_k == "l":
    lb_weight = weight * 2.2
    print(lb_weight)
else:
    kg_weight = weight * 0.45
    print(kg_weight)
