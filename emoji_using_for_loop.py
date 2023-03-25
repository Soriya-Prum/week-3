"""printing emojis using for loop"""
emoji = int(input("Please enter the number of rows: "))
for i in range(0, emoji):
    for j in range(0, i + 1):
        print("\U0001f600", end = " ")
    print()
        