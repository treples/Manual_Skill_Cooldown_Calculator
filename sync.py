loop = True
# breaks loop if tryAgain is equal to "n" by turning loop to False
while loop == True:
    # default values
    list1 = []
    list2 = []
    i = 0
    while True:
        first = input("Enter first timer cooldown in seconds: ")
        if first == "":
            print("Input is empty.")
            continue
        try:
            first = int(first)
        except ValueError:
            print("Incorrect input type.")
            continue
        else:
            firstInt = int(first)
            firstBase = int(first)
            break
    while True:
        second = input("Enter second timer cooldown in seconds: ")
        if second == "":
            print("Input is empty.")
            continue
        try:
            second = int(second)
        except ValueError:
            print("Incorrect input type.")
            continue
        else:
            secondInt = int(second)
            secondBase = int(second)
            break    
    while True:
        frequency = input("How many iterations? ")
        if frequency == "":
            print("Input is empty.")
            continue
        try:
            frequency = int(frequency)
        except ValueError:
            print("Incorrect input type.")
            continue
        else:
            frequencyInt = int(frequency)
            break
    while True:
        display = input("Display all activations and synchronizations? (Y/N) ")
        if display.lower() == "y" or "n":
            break
        else:
            print("(Y/N) only accepted.")
            continue

    # append every activation of both timers based on frequency
    while i < frequencyInt:
        list1.append(firstInt)
        list2.append(secondInt)
        # after appending activations, increment activation times
        firstInt += firstBase
        secondInt += secondBase 
        i += 1 
    
    # check for similar elements in both list1 and list2, then sort from lowest to highest
    sync = (sorted(set(list1) & set(list2))) 
    
    # visibility toggle for activations and synchronizations
    if display.lower() == "y":
        print("First Timer:", list1) 
        print("Second Timer:", list2)
        print("Synchronizations:", sync)

    # check for synchronizations, print synchronizations per hour when found
    if len(sync) == 0:
        print("No synchronizations found")
    else:
        common = sync[0] # gets first sync as "average time required to sync"
        average = 3600 / common # synchronizations per hour
        finalAverage = round(average, 2) # allows decimals for accuracy
        print("Both timers will synchronize " + str(finalAverage) + " per hour.")
    
    # replayability
    while True:
        tryAgain = input("Try again? (Y/N)\n")
        if tryAgain.lower() == "y":
            break
        elif tryAgain.lower() == "n":
            loop = False
            break
        else:
            print("(Y/N) only accepted.")
            continue
    








# TODO: append timers in a list
# TODO: check for similar numbers for sync
# TODO: append syncs in a list
# TODO: convert seconds to minutes
# TODO: (BONUS) allow user to pick how many timers to be used
# TODO: loop iterations until activations per hour is found
# TODO: find more ways to advance the scope of this program
# TODO:
# TODO:
# TODO:
# TODO: