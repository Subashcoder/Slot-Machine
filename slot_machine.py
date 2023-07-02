import random

MAX_LINE = 3
MIN_BET = 5
MAX_BET = 100

rows = 3
cols = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 6,
    "B" : 5,
    "C" : 4,
    "D" : 3
}

def get_slot_machine_spin(rows,cols,symbol):
    all_symbols = []
    for symbol,symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            values = random.choice(current_symbol)
            current_symbol.remove(values)
            column.append(values)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row],end="")
        print()

def check_wining(columns,lines,bet,values):
    wining = 0
    wining_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            wining += values[symbol] * bet
            wining_line.append(line+1)

    return wining,wining_line
def deposite():
    while True:
        amount = input("Please enter the Amount you what to deposite. $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Enter the Valid Amount")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the line you want to bet ( 1 -" + str(MAX_LINE) + "). ")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINE:
                break
            else:
                print("Enter line between (1 -" + str(MAX_LINE) + " )")
        else:
            print("Enter valid Number")
    return lines

def get_bet():
    while True:
        bet = input("Enter the about you want to bet: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("MINIMUM_BET = " + str(MIN_BET) + " And MAXIMUM_BET = " + str(MAX_BET) + " ")
        else:
            Print("Enter Valid Bet")

    return bet


def game(balance):
    line = get_number_of_lines()

    while True:
        betting = get_bet()
        total_bet = line * betting
        if total_bet > balance:
            print(f"Your Bet is higher than your balance. Your Plance is {balance}.")
        else:
            break

    print(f"Your Are betting ${total_bet} on line {line}. Your Balance is ${balance}")

    slot = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot = print_slot_machine(slot)
    wining, wining_line = check_wining(slot, line, betting, symbol_values)
    print(print_slot)
    print(f" Your Wining is {wining} on line {wining_line}")

    return wining - total_bet


def main():
    balance = deposite()
    while True:
        print(f'Your Current Balance is {balance}')
        spin = input(f"Press ENTER to play and Q to Quit")
        if spin == "q" or spin == "Q":
            break
        balance += game(balance)



main()
