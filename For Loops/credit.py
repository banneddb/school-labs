card_num = input("Insert your credit card number:")

if len(card_num)<13:
    print("INVALID")
if len(card_num) == 15:
    if "3" in card_num[0]:
        if "4" == card_num[1]:
            print("AMERICAN EXPRESS")
        elif "7" == card_num[1]:
            print("AMERICAN EXPRESS")
if len(card_num) == 16:
    if "5" == card_num[0]:
        if "1" == card_num[1]:
            print("MASTERCARD")
        elif "2" == card_num[1]:
            print("MASTERCARD")
        elif "3" == card_num[1]:
            print("MASTERCARD")
        elif "4" ==card_num[1]:
            print("MASTERCARD")
        elif "5" == card_num[1]:
            print("MASTERCARD")
if len(card_num) == 13 or len(card_num) == 16:
    if "4" == card_num[0]:
        print("VISA")