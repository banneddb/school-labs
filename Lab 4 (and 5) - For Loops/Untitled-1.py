total_bottles = (int(input("How many rounds of beers?")))
def bottlesofbeer(n):
    for bottles_left in range(total_bottles, 0, -1):
        print(bottles_left,"bottles of beer on the wall", bottles_left, "bottles of beer" )
        print("Take one down, pass it around", bottles_left-1, "bottles of beer on the wall")
bottlesofbeer(total_bottles)