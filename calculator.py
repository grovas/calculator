#!/user/bin/env python3
"""
This is a simple calculator application written for Python 3.x and for exercise :)
As input program expect 2 numbers.
As output user can choose from several mathematical operation.


Grovas - Artur Rozgowski <arczir@gmail.com>

"""
import sys

print("Calculator App\n")


# Function reads input from the user and checks if number is int/float type
def get_numbers():
    input_numbers = []
    for i in range(1, 3):
        while True:
            try:
                print("Enter number " + str(i) + " :")
                l = input()
                input_numbers.insert(i, float(l))
            except ValueError:
                print("You don't entered the number!")
                continue
            else:
                break
    return input_numbers


# Function takes only 1st letter entered by user
def get_decision():
    act=""
    while True: # loop control proper entered decision by user
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


# Function checks decision made by user
def chosen_action(act, list_number):
    result = [0,""]
    while act not in ('x', 'X', 'q', 'Q'):
        if act == 'a':
            result[0] = add(list_number)
            result[1] = 'addiction'
            break
        elif act == 's':
            result[0] = sub(list_number)
            result[1] = 'substract'
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


# Function print out formatted result
def print_result(numbers, result):
    doneCalculation = ""
    print("Result of {} number {} and number {} is: {}\n".
          format(result[1], numbers[0], numbers[1], result[0]))
    doneCalculation = input("Do you want to exit? Press 'y' or 'n' ")[0]
    return doneCalculation


# Function check if user want to calculate another set of numbers or exit program
def new_calculation():
    new_numbers = ""
    new_numbers = input("Do you want to check other numbers? ('y' or 'n')")[0]
    return new_numbers


# Function addiction
def add(numbers):
    result = 0
    result = numbers[0] + numbers[1]
    return result


# Function substrack
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
    first_calculation = ""
    whatCalculationToDo = ""
    end_program = ""
    decision = ""
    list_number = []  # program save input numbers to the list

    list_number = get_numbers()

    decision = get_decision()

    resultFromCalculation = chosen_action(decision, list_number)

    end_program = print_result(list_number, resultFromCalculation)
    while True:
        if end_program != 'y': # check if user want to end program
            if new_calculation() == 'y': # check if continue with a new numebers
                list_number = []

                list_number = get_numbers()
                decision = get_decision()

                resultFromCalculation = chosen_action(decision, list_number)

                end_program = print_result(list_number, resultFromCalculation)

            else:
                decision = get_decision() # else continue with old numbers

                resultFromCalculation = chosen_action(decision, list_number)

                end_program = print_result(list_number, resultFromCalculation)

        else:
            break

# The main entry
if __name__ == '__main__':
    sys.exit(main())