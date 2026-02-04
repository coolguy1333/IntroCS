#bro idk
import random
import time
import os

os.system('color')

#colors

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

RESET = '\033[0m' # called to return to standard terminal text color

#track sections
forwatrac = "----"
downtrac = "|"

forwatraceng = "><><"
downtraceng = "X"
forwatrackaremp = "CEMP"

#track ids
tid1 = forwatrac
tid2 = forwatrac
tid3 = forwatrac
tid4 = forwatrac
tid5 = forwatrac
tid6 = forwatrac
tid7 = forwatrac
tid8 = forwatrac
tid9 = forwatrac
tid10 = forwatrac
tid11 = forwatrac
tid12 = forwatrac
tid13 = forwatrac
tid14 = forwatrac
tid15 = forwatrac
tid16 = forwatrac
tid17 = forwatrac
tid18 = forwatrac
tid19 = forwatrac
tid20 = forwatrac
tid21 = forwatrac
tid22 = forwatrac
tid23 = forwatrac
tid24 = forwatrac
tid25 = forwatrac
tid26 = forwatrac
tid27 = downtrac
tid28 = downtrac
tid29 = downtrac
tid30 = downtrac
tid31 = downtrac
tid32 = downtrac

#switch arrangments
swp1 = RED + "|" + RESET
swp2 = RED + "/" + RESET
swp3 = RED + "-" + RESET
swp4 = RED + "\\" + RESET

waterm = 10000

coalm =16

coall = 10

waterl = 6000

times = 0

money = 10000

sid1 = swp3
sid2 = swp3
sid3 = swp3
sid4 = swp3
sid5 = swp3
sid6 = swp1

while True:

    #prices
    #coalp = 10
    #waterp = 10
    coalp = random.randint(4500,11500)/100
    waterp = random.randint(300,1000)/100

    #frame rate??
    #time.sleep(.1)

    #counters
    waterl = waterl - (times*250)
    coall = coall - (times*.25)
    #print(str(coalp)+str(waterp))

    #Coal water levels/price/refill warn/money

    print("\n\n")
    #money
    print(GREEN+"Money: $"+str(round(money, 2))+RESET+"\n")
    #coal
    if coall <= 1:
        print(BRIGHT_YELLOW+"\nREFIL YOUR"+BLACK+" COAL "+BRIGHT_YELLOW+"NOW!!")
    print(BLACK+"Coal: "+str(coall)+"t"+RESET)
    print(BLACK+"Coal Price:"+GREEN+" $"+str(coalp)+BLACK+" per ton\n"+RESET)
    #water
    if waterl <= 1000:
        print(BRIGHT_YELLOW+"\nREFIL YOUR"+BLUE+" WATER "+BRIGHT_YELLOW+"NOW!!")
    print(BLUE+"Water: "+str(waterl)+"gal"+RESET)
    print(BLUE+"Water Price:"+GREEN+" $"+str(waterp)+BLUE+" per 100 gal"+RESET)

    #map

    print("\n\n")
    print("      "+GREEN+"Farm "+RESET+tid19+"      "+BLACK+"Oil "+RESET+tid20+"                             "+GREEN+"Yard "+RESET+tid21+tid22+tid23+tid24+tid25)
    print("   "+tid1+tid2+tid3+ sid1+BLUE+"1"+RESET +tid4+tid5+tid6+ sid2+BLUE+"2"+RESET +tid7+tid8+tid9+tid10+tid11+ sid3+BLUE+"3"+RESET +tid12+tid13+ sid4+BLUE+"4"+RESET +tid14+tid15+tid16+tid17+tid18)
    print("               "+tid27+"                      "+YELLOW+"Saw Mill "+RESET+tid26)
    print("               "+tid27)
    print("               "+tid28)
    print("               "+tid28)
    print("               "+sid6+BLUE+"6"+RESET)
    print("               |\\")
    print("               | \\")
    print("               "+tid29+YELLOW+"L"+RESET+tid31)
    print("               "+tid29+YELLOW+"o"+RESET+tid31)
    print("               "+tid30+YELLOW+"g"+RESET+tid32)
    print("               "+tid30+YELLOW+"s"+RESET+tid32)
    #what action

    action = input(CYAN+"T = Train"+GREEN+"\nB = Shop"+RED+"\nS = Switch"+RESET+"\n"+CYAN+"Train "+GREEN+"Shop"+RESET+" Or "+RED+ "Switch"+ RESET+"?:")

    #Switches

    if action == "S" or action == "s":
        SWC = input("\n\n#'s only\nWhat switch id?:")

        if SWC == "1":
            pos = input("\n1="+RED + "/" + RESET+"\n2="+RED + "-" + RESET+"\n3="+RED + "\\" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid1 = swp2
            if pos == "2":
                sid1 = swp3
            if pos == "3":
                sid1 = swp4

        if SWC == "2":
            pos = input("\n1="+RED + "-" + RESET+"\n2="+RED + "\\" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid2 = swp3
            if pos == "2":
                sid2 = swp4

        if SWC == "3":
            pos = input("\n1="+RED + "/" + RESET+"\n2="+RED + "-" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid3 = swp2
            if pos == "2":
                sid3 = swp3

        if SWC == "4":
            pos = input("\n1="+RED + "/" + RESET+"\n2="+RED + "-" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid4 = swp2
            if pos == "2":
                sid4 = swp3

        if SWC == "5":
            pos = input("\n1="+RED + "-" + RESET+"\n2="+RED + "\\" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid5 = swp3
            if pos == "2":
                sid5 = swp4

        if SWC == "6":
            pos = input("\n1="+RED + "|" + RESET+"\n2="+RED + "\\" + RESET+"\nWhat postion?:")
            if pos == "1":
                sid6 = swp1
            if pos == "2":
                sid6 = swp4

    #shop

    if action == "B" or action == "b":
        #info
        #money
        print(GREEN+"\n\nMoney: $"+str(round(money, 2))+RESET+"\n")
        #coal
        if coall <= 1:
            print(BRIGHT_YELLOW+"\nREFIL YOUR"+BLACK+" COAL "+BRIGHT_YELLOW+"NOW!!")
        print(BLACK+"Coal: "+str(coall)+"t"+RESET)
        print(BLACK+"Coal Price:"+GREEN+" $"+str(coalp)+BLACK+" per ton\n"+RESET)
        #water
        if waterl <= 1000:
            print(BRIGHT_YELLOW+"\nREFIL YOUR"+BLUE+" WATER "+BRIGHT_YELLOW+"NOW!!")
        print(BLUE+"Water: "+str(waterl)+"gal"+RESET)
        print(BLUE+"Water Price:"+GREEN+" $"+str(waterp)+BLUE+" per 100 gal"+RESET)

        #what you buying

        buying = input(BLACK+"\n\nC = Coal"+BLUE+"\nW = Water"+RESET+"\n\nWhat would you like to buy?:")
        #coal
        if buying == "C" or buying == "c":
            amountstr = input("\nHow much "+BLACK+"Coal"+RESET+" (in tons)?:")
            amount = int(amountstr)
            if coalm < amount+coall:
                print(RED+"\nYour out of storage!!"+RESET)
                refunda = (coall+amount) - coalm
                print(BLACK+str(refunda)+RESET+" tons of coal were refunded")
                coall = (amount+coall) - refunda
                money = money - ((amount-refunda)*coalp)
            else:
                if money < money - (amount*coalp):
                    print(RED+"\nYour Broke"+RESET+"\nYou have "+GREEN+"$"+str(money)+RESET)
                else:
                    money = money - (amount*coalp)
                    coall = coall + amount
        #water
        if buying == "W" or buying == "w":
            amountstr = input("\nHow much "+BLUE+"Water"+RESET+" (gal)?:")
            amount = int(amountstr)
            if waterm < amount+waterl:
                print(RED+"\nYour out of storage!!"+RESET)
                refunda = (waterl+amount) - waterm
                print(BLUE+str(refunda)+RESET+" gallons of water were refunded")
                waterl = (amount+waterl) - refunda
                money = money - ((amount-refunda)*(waterp/100))
            else:
                if money < money - (amount*(waterp/100)):
                    print(RED+"\nYour Broke"+RESET+"\nYou have "+GREEN+"$"+str(money)+RESET)
                else:
                    money = money - (amount*(waterp/100))
                    waterl = waterl + amount



    #train

    if action == "T" or action == "t":

        times = times + 1

        print(CYAN+"\n\nTrain"+RESET)


    print("\n\n")
    input(MAGENTA+"Hit enter to continue"+RESET)