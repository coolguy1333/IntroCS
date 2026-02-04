from os import *
from sys import *
from keyboard import *
from random import *
from time import *

system('color')

# colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[192m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[43m'

R = '\033[0m' # called to return to standard terminal text color

# VARS
sid1 = "\\"
sid2 = "\\"
sid3 = "/"
sid4 = "/"
sid5 = "\\"

waterm = 10000

coalm = 16

coall = 10

coalp = 100

waterl = 6000

waterm = 16000

waterp = 10

times = 0 

money = 10000



def create_matrix(rows, cols, default_value=" "):
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(''.join(str(cell) for cell in row))

def create_map(matrix, train_pos):
    # First row
    farm_text = GREEN + "Farm ----" + R
    oil_text = BLACK + "Oil ----" + R
    yard_text = RED + "Yard ---------------------"

    # Add Farm
    start_farm = 3
    for i, char in enumerate(farm_text):
        matrix[0][start_farm + i] = char

    # Add Oil
    start_oil = 18
    for i, char in enumerate(oil_text):
        matrix[0][start_oil + i] = char

    # Add Yard
    start_yard = 54
    for i, char in enumerate(yard_text):
        if i < 84:
            matrix[0][start_yard + i] = char
        else:
            print("help")

    # Second row (dashes, numbers and slashes)
    dashes = "------------\\1------------\\2--------------------/3--------/4--------------------\\5----"
    for i, char in enumerate(dashes):
        matrix[1][i] = char

    # Third row (Saw Mill)
    saw_mill = "                                   " + YELLOW + "Saw Mill ----" + R
    for i, char in enumerate(saw_mill):
        matrix[2][i] = char

    # switches
    # sid1
    matrix[1][12] = RED+sid1+R
    matrix[1][13] = BLUE+"1"+R

    # sid2
    matrix[1][26] = RED+sid2+R
    matrix[1][27] = BLUE+"2"+R

    # sid3
    matrix[1][48] = RED+sid3+R
    matrix[1][49] = BLUE+"3"+R

    # sid4
    matrix[1][58] = RED+sid4+R
    matrix[1][59] = BLUE+"4"+R

    # sid5
    matrix[1][80] = RED+sid5+R
    matrix[1][81] = BLUE+"5"+R

    # Add train
    matrix[1][train_pos] = BRIGHT_CYAN+"T"+R

def shop_interface():
    system('cls')

    global money, coall, waterl, coalm, waterm, coalp, waterp

    # Display user's balance and available resources
    print(GREEN + "\n\nMoney: $" + str(round(money, 2)) + R + "\n")
    if coall <= 1:
        print(BRIGHT_YELLOW + "\nREFILL YOUR" + BLACK + " COAL " + BRIGHT_YELLOW + "NOW!!")
    print(BLACK + "Coal: " + str(coall) + "t" + R)
    print(BLACK + "Coal Price: " + GREEN + " $" + str(coalp) + BLACK + " per ton\n" + R)

    if waterl <= 1000:
        print(BRIGHT_YELLOW + "\nREFILL YOUR" + BLUE + " WATER " + BRIGHT_YELLOW + "NOW!!")
    print(BLUE + "Water: " + str(waterl) + "gal" + R)
    print(BLUE + "Water Price: " + GREEN + " $" + str(waterp) + BLUE + " per 100 gal" + R)

    print("\nWhat would you like to buy?")
    print(BLACK + "\nC = Coal" + BLUE + "\nW = Water" + R)

    # Wait for user to input their choice
    read_event()
    event = read_event()
    if event.event_type == KEY_DOWN:
        if event.name == 'c':  # User wants to buy coal
            amount = eval(input("\nHow much " + BLACK + "Coal" + R + " (in tons)?: "))
            if coalm < amount + coall:
                print(RED + "\nYour storage is full!" + R)
                refunda = (coall + amount) - coalm
                print(BLACK + str(refunda) + R + " tons of coal were refunded")
                coall = (amount + coall) - refunda
                money -= ((amount - refunda) * coalp)
                sleep(1)
            else:
                if money < (amount * coalp):
                    print(RED + "\nYou don't have enough money!" + R)
                    print(BLACK + "You have $" + str(round(money, 2)) + R)
                    sleep(1)
                else:
                    money -= (amount * coalp)
                    coall += amount
                    print(BRIGHT_GREEN + f"\nSuccessfully bought {amount} tons of coal!" + R)
                    sleep(1)

        elif event.name == 'w':  # User wants to buy water
            amountstr = input("\nHow much " + BLUE + "Water" + R + " (in gallons)?: ")
            amount = int(amountstr)
            if waterm < amount + waterl:
                print(RED + "\nYour storage is full!" + R)
                refunda = (waterl + amount) - waterm
                print(BLUE + str(refunda) + R + " gallons of water were refunded")
                waterl = (amount + waterl) - refunda
                money -= ((amount - refunda) * (waterp / 100))
                sleep(1)
            else:
                if money < (amount * (waterp / 100)):
                    print(RED + "\nYou don't have enough money!" + R)
                    print(BLACK + "You have $" + str(round(money, 2)) + R)
                    sleep(1)
                else:
                    money -= (amount * (waterp / 100))
                    waterl += amount
                    print(BRIGHT_BLUE + f"\nSuccessfully bought {amount} gallons of water!" + R)
                    sleep(1)

        else:
            print(RED + "\nInvalid selection! Please choose 'C' for Coal or 'W' for Water." + R)

def main():
    global money, coall, waterl, coalm, waterm, coalp, waterp, sid1, sid2, sid3, sid4, sid5, train_pos
    coalp = randint(4500, 11500) / 100
    waterp = randint(300, 1000) / 100
    train_pos = 0
    while True:
        system('cls')  # Clear the screen before printing the updated map

        print("\n\n")
        #money
        print(GREEN+"Money: $"+str(round(money, 2))+R+"\n")
        #coal
        if coall <= 1:
            print(BRIGHT_YELLOW+"\nREFILL YOUR"+BLACK+" COAL "+BRIGHT_YELLOW+"NOW!!")
        print(BLACK+"Coal: "+str(coall)+"t"+R)
        print(BLACK+"Coal Price:"+GREEN+" $"+str(coalp)+BLACK+" per ton\n"+R)
        #water
        if waterl <= 1000:
            print(BRIGHT_YELLOW+"\nREFILL YOUR"+BLUE+" WATER "+BRIGHT_YELLOW+"NOW!!")
        print(BLUE+"Water: "+str(waterl)+"gal"+R)
        print(BLUE+"Water Price:"+GREEN+" $"+str(waterp)+BLUE+" per 100 gal\n\n"+R)

        # Create and print the map
        matrix = create_matrix(3, 86)
        create_map(matrix, train_pos)
        print_matrix(matrix)
        print("\nPress S to buy coal and water")
        print("Use left/right arrow keys to move train (q to quit)")

        # Wait until a key is pressed
        event = read_event()

        if event.event_type == KEY_DOWN:
            if event.name == 'left' and train_pos > 0:  # Left arrow
                train_pos -= 1
                coall -= .1
                waterl -= 100
            elif event.name == 'right' and train_pos < 85:  # Right arrow
                train_pos += 1
                coall -= .1
                waterl -= 100
            elif event.name == 'q':  # Quit
                break
            elif event.name == 's':  # Open the shop
                shop_interface()
            elif event.name == '1':  # Change sid1
                sid1 = "-" if sid1 == "\\" else "\\"
            elif event.name == '2':  # Change sid2
                sid2 = "-" if sid2 == "\\" else "\\"
            elif event.name == '3':  # Change sid3
                sid3 = "-" if sid3 == "/" else "/"
            elif event.name == '4':  # Change sid4
                sid4 = "-" if sid4 == "/" else "/"
            elif event.name == '5':  # Change sid5
                sid5 = "-" if sid5 == "\\" else "\\"

            print("Press any key to continue!")
            event = read_event()

while True:
    main()