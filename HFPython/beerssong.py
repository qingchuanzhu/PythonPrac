word = "bottles"
for num_beer in range(10, 0, -1):
    print(num_beer, word, "of beer on the wall")
    print(num_beer, word, "of beer")
    print("Take one down")
    print("Pass it around")

    if(num_beer == 1):
        print("No more bottles of beer on the wall.")
    else:
        new_num = num_beer - 1
        if(new_num == 1):
            word = "bottle"
        print(new_num, word,"of beer on the wall")
    print()
