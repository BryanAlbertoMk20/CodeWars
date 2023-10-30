def opposite(number):
    if number == 0:
        return 0
    if number < 0:
        positive_number = (number - number) - number
        return positive_number
    elif number > 0:
        negative_number = number - number - number
        return negative_number

print(opposite(-95858588225))




