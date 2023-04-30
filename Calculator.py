## Calculator Program
import sys

#for line in sys.stdin:      This gets input from the command line and outputs the int
#    print(int(line))

def askInt():
    for line in sys.stdin:
        return int(line)

def askStr():
    for line in sys.stdin:
        return str(line)

def main():
    print("##### Calculator #####")
    print("     Please enter your first number! [ warning, if what you enter isnt an integer, this will break! ] ")
    num1 = askInt()
    
    print("     Please enter your second number! [ warning, if what you enter isnt an integer, this will break! ] ")
    num2 = askInt()

    print("    Please enter your operator! [add - subtract - multiply - divide]")
    opl = input()
    
    print("Calculating.")
    print("Calculating..")
    print("Calculating...")
    
    if opl == "add":
        print(num1 + num2)
    elif opl == "subtract":
        print(num1 - num2)
    elif opl == "multiply":
        print(num1 * num2)
    elif opl == "divide":
        print(num1 / num2)
    else:
        print("idk you messed up lol")
    
    input("Press enter to leave :)")

if __name__ == '__main__':
    main()