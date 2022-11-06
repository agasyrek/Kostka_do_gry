import random


def get_code():
    """The function retrieves the code from the user and extracts the number of throws
    rtype: str, int
    return: a list with code elements and the number of throws"""
    while True:
        try:
            dice_code = input('enter the dice roll code ')
            splited_code = dice_code.split('D')
            num_of_throws = splited_code[0]
            if num_of_throws == '':
                num_of_throws = 1
            else:
                num_of_throws = int(num_of_throws)
            break
        except ValueError:
            print('You entered the wrong code')
    return [splited_code, num_of_throws]


def dice():
    """The main function of the program
    :rtype: int
    return: the result of the dice roll"""
    while True:
        try:
            code = get_code()
            print(code)
            splited_code = code[0]
            num_of_throws = code[1]
            if '+' in splited_code[1]:
                splited_code_2 = splited_code[1].split('+')
                type_of_dice = int(splited_code_2[0])
                modification = int(splited_code_2[1])
                add = True
                subtract = False
            elif '-' in splited_code[1]:
                splited_code_2 = splited_code[1].split('-')
                type_of_dice = int(splited_code_2[0])
                modification = int(splited_code_2[1])
                subtract = True
                add = False
            else:
                type_of_dice = int(splited_code[1])
                modification = 0
                subtract = False
                add = False
            if type_of_dice >= 1 and type_of_dice <= 100:
                break
            else:
                print('You entered the wrong code')
        except ValueError:
            print('You entered the wrong code')

    throw = 0
    for i in range(0, num_of_throws):
        throw = throw + random.randint(1, type_of_dice)
    if subtract == True:
        result = throw - modification
    elif add == True:
        result = throw + modification
    else:
        result = throw
    print(f'The result is {result}')
    return result


if __name__ == '__main__':
    dice()
