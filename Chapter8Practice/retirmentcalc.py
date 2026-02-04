marketgrowth = .1
numyears = int(input("How may years do you plan to work for?:"))
paycheckperyear = eval(input("How many times do you get payed per year?:"))
savingsperpaycheck = eval(input("How much do you save per paycheck?:"))

total = 0
mysavings = 0
for i in range(numyears):
    for j in range(paycheckperyear):
        growth = (1 + marketgrowth) ** (1/ paycheckperyear)
        total = total * growth
        total = total + savingsperpaycheck
        mysavings = mysavings +savingsperpaycheck
print("Your life's savings total to: " + str(total))
print("Your life's savings total to without investments: " + str(mysavings))
