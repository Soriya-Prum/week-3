"""printing emojis using while loop"""
emoji = int(input("Please enter the number of rows: "))
i = 1
while i <= emoji:
    j = 1
    while j <= i:
        print("\U0001f600", end = " ")
        j = j + 1
    print()
    i = i + 1