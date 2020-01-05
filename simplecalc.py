def add(num1,num2):
    ans = num1 + num2
    return ans

def sub(num1,num2):
    ans = num1 - num2
    return ans

def mult(num1,num2):
    ans = num1 * num2
    return ans

def div(num1,num2):
    ans = num1/num2
    return ans


print("""
To:
Add - enter 1
Subtract - enter 2
Divide - enter 3
Multiply - enter 4
Quit - enter q
""")

quit = False
while not quit:

    command = input("Enter your choice here: ")

    print("Please enter numbers for calculation")
    a = int(input('>'))
    b = int(input('>'))

    if command == '1':
        print (add(a,b))
    elif command == '2':
        print (sub(a,b))
    elif command == '3':
        print (div(a,b))
    elif command == '4':
        print (mult(a,b))
    else:
        break









