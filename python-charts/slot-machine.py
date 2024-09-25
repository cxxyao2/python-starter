MAX_LINE3 = 3
MIN_BET = 1
MAX_BET = 3

def deposit():
    while True:
        amount = input("How much would you like to deposit? ")
        if amount.isdigit():
            amount =  int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a  number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play? (1-" + str(MAX_LINE3) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINE3:
                break
            else:
                print("Please enter a number between 1 and {MAX_LINE3}.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        bet = input("How much would you like to bet per line? (1-" + str(MAX_BET) +")? ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0 and bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return bet



def main():
    balance = deposit()
    lines = get_number_of_lines()   
    bet = get_bet()
    print(balance, lines)


main()