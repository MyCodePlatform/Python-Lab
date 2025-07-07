n1 = 10
n2 = 20

if n1 < n2 :

    print("in if number before swap:", n1, n2 )

    n2 = n2 + n1
    n1 = n2 - n1
    n2 = n2 - n1

    print ("in if , number after swap", n1, n2)
else:
    print ("in else, before swap", n1, n2)

    n1 = n1 + n2
    n2 = n1 - n2
    n1 = n1 - n2

    print ("in else : numbers after swap", n1, n2)
    
