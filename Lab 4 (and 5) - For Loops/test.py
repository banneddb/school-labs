card_num = input("Insert your credit card number:")

def checksum(card_num):
    every_other_num = card_num[::2]*2
    print(every_other_num)


checksum(card_num)