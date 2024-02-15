choice = ''

history = []

while choice == '':
    num = int(input("Enter a number: "))
    op = input("Enter an operation (type history to view calculator history: ")
    num2 = int(input("Enter a number: "))
 
    if op == '+':
        print(num, "+", num2, "=", num + num2)
        history.append(str(num) + " " + op + " " + str(num2) + " = " + str(num+num2))
 
    elif op == '-':
        print(num, "-", num2, "=", num - num2)
        history.append(str(num) + " " + op + " " + str(num2) + " = " + str(num-num2))
        
    elif op == '*':
        print(num, "*", num2, "=", num * num2)
        history.append(str(num) + " " + op + " " + str(num2) + " = " + str(num*num2))
 
    elif op == '/':
        print(num, "/", num2, "=", num / num2)
        history.append(str(num) + " " + op + " " + str(num2) + " = " + str(num/num2))

    elif op == 'history':
        for i in history:
            print(i)

    choice = input("Would you like to try again? ")
