def search():
    
def info():
    

def write():
    entry = input("\nPlease enter the question info: ")
    with open("satProblemsInfo.txt", "a") as data:
        

def intro():
    print("Welcome to Abby's SAT Database! What would you like to do?\n\tA. Search for specific question information\n\tB. See useful info for questions answered\n\tC. Add info about questions answered\n\t?: See these options again")
    return

def main():
    input = input("What would you like to do? ").upper()
    match input:
        case "A":
            search()
        case "B":
            info()
        case "C":
            write()
        case "?":
            intro()
        case _:
            print("Sorry, that's not an option. Please enter the letter that appears before the option you want to do. Press question mark to see your options.")
            return        

intro()
while True:
    main()