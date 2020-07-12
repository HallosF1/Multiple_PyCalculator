import calculator


while True:
    print("pls choose a option\n 1 : sum \n 2 : sub \n 3 : multiply \n 4 : divide")

    options = input("What is your choice ?")
    if options == "1" or options == "2" or options == "3" or options == "4":
        break
    else:
        print("*** pls choose a correct option ***")
        continue

hm_numbers = int(input("How many numbers will you use ?"))
choosen = list(map(lambda nums: int(input('enter a number : ')), range(1, hm_numbers + 1)))
while True:
    if options == '1':
        print(calculator.sum(choosen))
        break
    elif options == '2':
        print(calculator.sub(choosen))
        break
    elif options == '3':
        print(calculator.multiply(choosen))
        break
    elif options == '4':
        print(calculator.divide(choosen))
        break
