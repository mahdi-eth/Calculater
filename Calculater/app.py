def calculater(left_hand,operator,right_hand):
    result = 0
    if operator == "+": result = left_hand + right_hand
    elif operator == "-": result = left_hand - right_hand
    elif operator == "*": result = left_hand * right_hand
    elif operator == "/": result = left_hand / right_hand
    print(result)

left_hand = int(input("Enter the left hand number : "))
operator = input("Enter the operator : ")
right_hand = int(input("Enter the right hand number : "))
calculater(left_hand,operator,right_hand)
