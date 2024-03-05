def parent_func(selection, numbers):
    def sumCustom():
        return numbers[0] + numbers[1] + numbers[2]

    def subCustom():
        return numbers[0] - numbers[1] - numbers[2]

    def multiCustom():
        return numbers[0] * numbers[1] * numbers[2]

    def divCustom():
        return numbers[0] / numbers[1]

    def expCustom():
        return numbers[0] ** numbers[1]

    def floordivCustom():
        return numbers[0] // numbers[1]

    for op in selection:
        match op:
            case 1:
                print(sumCustom())
            case 2:
                print(subCustom())
            case 3:
                print(multiCustom())
            case 4:
                print(divCustom())
            case 5:
                print(expCustom())
            case 6:
                print(floordivCustom())
            case default:
                print("Invalid argument")


while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n6To9. Floor Division")
    selection = input("Enter the operations you want to perform: ")
    operators = [int(op) for op in selection.split()]
    print(operators)

    args = input("Enter the elements separated by space: ")
    numbers = [int(num) for num in args.split()]

    if len(numbers) > 3:
        print("Please enter maximum 3 arguments")
    else:
        parent_func(operators, numbers)

    answer = input("Want to try again? Y/n : ")
    if answer.lower() != "y":
        break

