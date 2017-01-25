#!/user/bin/env python3
"""
This is a simple calculator application written for Python 3.x and for exercise :)
As input program expect 2 numbers.
As output user can choose from several mathematical operation.

Logic layer:
    -

ver. 0.2

Grovas - Artur Rozgowski <arczir@gmail.com>

"""

print("Calculator App\n")


def get_numbers():
    """
    Function reads input from the user and checks if number is int/float type
    :return: list of 2 numbers
    """
    input_numbers = []  # empty list to store 2 numbers
    for i in range(1, 3):
        while True:
            try:
                print("Enter number " + str(i) + " :")
                l = input()
                # to list we save variable float from input
                input_numbers.insert(i, float(l))
            except ValueError:  # if not numbers entered program will wait for correction
                print("You don't entered the number!")
                continue
            else:
                break
    return input_numbers


def get_decision():
    """
    Function ask user to make a decision what calculation todo.
    Function takes only 1st letter entered by user and lower this letter
    :return:
    """
    while True:  # loop control proper entered decision by user
        act = input("\nWhat do you want to calculate with 2 digits:\n"
                    "Press 'A' for Addiction or\n"
                    "Press 'S' for Subtract or\n"
                    "Press 'M' for Multiply or\n"
                    "Press 'D' for Divide or\n"
                    "Press '%' for Modulo\n").lower()[0]
        if act not in ('a', 's', 'm', 'd', '%'):
            print("Please make a correct decision!")
        else:
            break
    return act


def chosen_action(act, list_number):
    """
    Function checks decision made by user
    :param act:
    :param list_number:
    :return: list with calculation result and name of calculation required for print result
    """
    result = [0,""]  # list to store result and name of mathematical function
    while act not in ('x', 'X', 'q', 'Q'):
        if act == 'a':
            result[0] = add(list_number)
            result[1] = 'addiction'
            break
        elif act == 's':
            result[0] = sub(list_number)
            result[1] = 'subtract'
            break
        elif act == 'm':
            result[0] = mul(list_number)
            result[1] = 'multiply'
            break
        elif act == 'd':
            result[0] = div(list_number)
            result[1] = 'divide'
            break
        elif act == '%':
            result[0] = mod(list_number)
            result[1] = 'modulo'
            break
    return result


def print_result(numbers, result):
    """
    Function print out formatted result
    Output printed 'result' is formatted to 2 digits after decimal dot
    Function returns answer 'on exit from program' - it takes first lower letter [0]
    """
    print("Result of {0} number {1} and number {2} is: {3:0.2f}\n".
          format(result[1], numbers[0], numbers[1], result[0]))
    calculation_done = input("Do you want to exit? Press 'y' or 'n' ")[0].lower()
    return calculation_done


def other_numbers():
    """
    Function check and return if user want to calculate another set of numbers
    """
    new_numbers = input("Do you want to check other numbers? ('y' or 'n')")[0].lower()
    return new_numbers


# Function addiction
def add(numbers):
    result = 0
    result = numbers[0] + numbers[1]
    return result


# Function subtract
def sub(numbers):
    result = 0
    result = numbers[0] - numbers[1]
    return result


# Function multiply
def mul(numbers):
    result = 0
    result = numbers[0] * numbers[1]
    return result


# Function multiply
def div(numbers):
    result = 0
    result = numbers[0] / numbers[1]
    return result


# Function multiply
def mod(numbers):
    result = 0
    result = numbers[0] % numbers[1]
    return result


# Main function
def main():
    end_program = 'n'
    first_calculation = True
    list_number = []  # global list of calculated input numbers
    new_numbers = ""
    while True:
        if end_program == 'n':  # checks if user want to end program

            if first_calculation: # checks if it is first loop of program
                list_number = get_numbers()
            if not first_calculation:
                new_numbers = other_numbers()  # check if user want to new numbers
            if new_numbers == 'y':
                list_number = get_numbers()
            decision = get_decision()
            calculation_result = chosen_action(decision, list_number)
            end_program = print_result(list_number, calculation_result)
            first_calculation = False
        else:
            break

if __name__ == '__main__':
    """ The main entry of program """
    main()