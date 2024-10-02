num = int(input("What is the integer for the multiplication table?"))

def multiplication_table(num):
    for row in range(1, num+1):
        for collum in range(1, num+1):
            print(row*collum, end="  ")
        print()

multiplication_table(num)