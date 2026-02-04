""" lists are intended to be a set of related info
 the lists in this project will be used to calculate your taxes

 taxes use multiple lists (your income "bracket", the actual percentage, and a flat dollar amount)

 when you have multiple lists that are related to each other, you call those "parallel arrays"
 """

wiBrackets = [0, 19090, 38190, 420420]
wiPercents = [0.035, 0.044, 0.053, 0.0765]
wiFlat = [0, 668.15, 1508.55, 21766.74]

fedBrackets = [0, 11601, 47151, 100526, 191951, 243726, 609351]
fedPercents = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
fedFlat = [0, 1160.1, 5426.1, 17168.6, 39110.6, 55678.6, 183647.35]

ssBrackets = [0, 168600]
ssPercents = [0.062, 0]
ssFlat = [0, 10453.2]

medBrackets = [0, 200000]
medPercents = [0.0145, 0.0235]
medFlat = [0, 2900]

##################
# Helper Methods #
##################
def calculateTax(salary, type):
    brackets = []
    percents = []
    flat = []
    if type == "wisconsin":
        brackets = wiBrackets
        percents = wiPercents
        flat = wiFlat

    if type == "federal":
        brackets = fedBrackets
        percents = fedPercents
        flat = fedFlat

    if type == "medicare":
        brackets = medBrackets
        percents = medPercents
        flat = medFlat
   
    if type == "social_security":
        brackets = ssBrackets
        percents = ssPercents
        flat = ssFlat

    tax = 0
    index = 0
    for i in range(len(brackets)):
        if salary >= brackets[i]:
            index = i

    tax = flat[index] + (salary - brackets[index]) * percents[index]
    return tax

###################
# Executable code #
###################
salary = eval(input("How much moneys do you make?"))
wiTax = calculateTax(salary, "wisconsin")
fedTax = calculateTax(salary, "federal")
ssTax = calculateTax(salary, "social_security")
medTax = calculateTax(salary, "medicare")
remainingSalary = salary - wiTax - fedTax - ssTax - medTax

print("Your Wisconsin state income tax will be: $"+str(wiTax))
print("Your Federal income tax will be: $"+str(fedTax))
print("Your Social Security contribution will be: $"+str(ssTax))
print("Your Medicare contribution will be: $"+str(medTax))
print("Your take-home pay for the year should be: $"+str(remainingSalary))