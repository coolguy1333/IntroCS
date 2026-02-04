# counting the number of times a loop runs
count1 = 0
for i in range(10): # this loop should run 10 times
    count1 += 1
print(count1)

# asking a USER how many times they want the loop to run
numRuns = eval(input("How many times would you like this loop to run?"))
count2 = 0
for i in range(numRuns):
    count2 += 1
print(count2)

# looping through a list
numList1 = [5, 20, 3, 17, 42, 5, 89, 746, 2, -5]
total1 = 0
for num in numList1: # num is a LOCAL variable that takes turns being each item
    total1 += num
print(total1)

# nested for loops
count3 = 0
for i in range(10): # this loop will run 10 times
    for j in range(5): # this loop will run 5 times, for EACH outter loop
        count3 += 1
print(count3) # this should print out 50 because 10 * 5 is 50

# using the loop index
for i in range(10):
    print(i) # i is different numbers as the loop runs, it goes up by 1 each time
    # this printed 0 - 9, which is 10 numbers, but it starts at 0

# while loop to make sure a user enters something "valid"
answer = eval(input("What would you like to talk about? 1: video games\n2: movies\n3: your interests"))
while(not(answer == 1 or answer == 2 or answer == 3)):
    answer = eval(input("Your options were 1, 2, or 3. Please select one of those."))
print("Great, you selected option " + str(answer))