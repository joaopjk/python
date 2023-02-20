two_digit_number = input("Type a two digit number: ")
if len(two_digit_number) >= 2:
    first_digit = two_digit_number[0]
    second_digit = two_digit_number[1]
    if first_digit.isdigit() and second_digit.isdigit():
        print(int(first_digit) + int(second_digit))
    else:
        print("One of this values not a int")
