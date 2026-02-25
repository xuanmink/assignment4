numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit):")
    if user_input == "":
     break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input.")
numbers.sort(reverse=True)
print(f"The five greatest numbers are:{numbers[:5]}")