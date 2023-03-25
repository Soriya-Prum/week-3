for num in range(1, 21):
    if num == 4 or num == 13:
        print(num, ": Unlucky")
    elif num % 2 == 0:
        print(num, ": Even number")
    else:
        print(num, ": Odd number")
