import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS =3
COLS = 3

#symbols
symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checkWinning(columns, lines, bet, values):
    winning = 0
    winningLines = []
    for line in range(lines):
        #check if every symbols in the line are the same
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        # for-break means if if no break in the if will run the else
        else:
             winning += values[symbol] * bet   
             winningLines.append(lines+1)
             
    return winning, winningLines
        
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        #do the copy by adding the [:]
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def printSlothMachine(columns):
    #transposing in matrix 
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end =" ")
                
        print()
        

def deposit():
    while True:
        amount = input("What would you like to deposit ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("amount must be a number.")
    return amount

#collect the bet
def getNumberOfLine():
    while True:
        lines = input("emter the number of line to bet on (1-" + str(MAX_LINES) + ") ?  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter the valid number of line")
        else:
            print("pls, enter the number")
            
    return lines

def getBet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <+ MAX_BET :
                break
            else:
                print(f"amount must between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("amount must be a number.")
    return amount

def spin(balance):
    lines = getNumberOfLine()
    
    while True:
        bet = getBet()
        totalBet = bet * lines
        
        if totalBet > balance:
            print(f'you do not have enough to bet that anount, your current balnce is: ${balance}')
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is: ${totalBet}")
    
    slots = getSlotMachineSpin(ROWS, COLS, symbolCount )
    printSlothMachine(slots)
    
    winning, winningLines= checkWinning(slots, lines, bet, symbolValue)
    print(f"you won !!! ${winning}." )
    print(f"you won on lines", *winningLines)
    return winning - totalBet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        ans = input('press enter to play (q to quit)')
        if ans == 'q':
            break
        balance += spin(balance)
    
    print(f"you totally got ${balance}")
    
main()
        
