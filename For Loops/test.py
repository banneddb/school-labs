card_num = input("Insert your credit card number:")
x = list(str(card_num))

if "3" in card_num[0]:
    if "4" in card_num[1]:
        print("AMERICAN EXPRESS")
    elif "7" in card_num[1]:
        print("AMERICAN EXPRESS")
elif "5" in card_num[0]:
    if "1" in card_num[1]:
        print("MASTERCARD")
    if "2" in card_num[1]:
        print("MASTERCARD")
    if "3" in card_num[1]:
        print("MASTERCARD")
    if "4" in card_num[1]:
        print("MASTERCARD")
    if "5" in card_num[1]:
        print("MASTERCARD")
elif "4" in card_num[0]:
    print("VISA")
else:
    print("INVALID")