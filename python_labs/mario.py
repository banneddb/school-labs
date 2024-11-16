height = input("Pick a number between 1 and 8 for the height of you mario tower:")
height = int(height)

while height<1 or height>8:
    print("That is an invalid number!")
    height = int(input("Please pick a number between 1 and 8 for the height for your maruo tower?"))

def mario(height):
    true_height = height+1
    for i in range(1, true_height):
        spaces = ' ' * (height-i)
        hashs = '#'*i
        print(spaces + hashs)

mario(height)