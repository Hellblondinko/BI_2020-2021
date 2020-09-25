def decimalToBinary(num):
    """This function converts decimal number
    to binary"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# decimal number
number = int(input("Type any decimal number here: "))

decimalToBinary(number)
