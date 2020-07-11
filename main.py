import calculator


while True:
    print("pls choose a option\n 1 : sum \n 2 : sub \n 3 : multiply \n 4 : divide")

    options = input("What is your choice ?")
    choosen = list(map(lambda nums: int(input('enter a number : ')), range(1,3)))
    num1 = choosen[0]
    num2 = choosen[1]


    if options == '1':
        print(calculator.sum(num1, num2))
        break
    elif options == '2':
        print(calculator.sub(num1, num2))
        break
    elif options == '3':
        print(calculator.multiply(num1, num2))
        break
    elif options == '4':
        print(calculator.divide(num1, num2))
        break

    else:
        print("pls choose a correct option")
        continue
