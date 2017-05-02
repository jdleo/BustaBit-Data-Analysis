# same source code for tests 1 and 2. only things changed are base bets and starting balance

import random
import requests
import time

#max random value
max = 100000000

#probabilities for each multiplier (1.1x , 1.12x , etc) out of 100,000,000
p_1_06 = 93352192
p_1_08 = 91607292
p_1_1 = 89926424
p_1_12 = 88306128
p_1_16 = 85234610
p_1_2 = 82369581
p_1_24 = 79690896
p_1_3 = 75984343
p_1_36 = 72607261
p_1_42 = 69517590

#array for all the multipliers we're testing
multipliers = [1.06, 1.08, 1.1, 1.12, 1.16, 1.2, 1.24, 1.3, 1.36, 1.42]

#array for all the probabilities
probs = [p_1_06,p_1_08,p_1_1,p_1_12,p_1_12,p_1_16,p_1_2,p_1_24,p_1_3,p_1_36,p_1_42]

#outer loop: looping through all the multipliers we're testing
index = 0
for multiplier in multipliers:
    #inner loop: 10 test cases
    for _ in range(0,10):
        #inner inner loop: generating a batch of 1000 random numbers
        #then, looping through them to see if win or loss
        random.seed(time.time())
        result = [random.randint(1,100000000) for _ in range(0,1000)]

        totalBalance = 15000
        base_bet = 500
        bet = base_bet
        
        losses = 0

        for i in result:
            if (i <= probs[index]):
                totalBalance += (bet * multiplier)
            else:
                totalBalance -= bet
                losses += 1
        
        lossPct = losses / 1000.0
        print("Multiplier: {}x".format(multiplier))
        print("Total Balance: {} bits".format(totalBalance))
        print("Loss percentage: {}".format(lossPct))
        print("-----------------------------------")
    
    print("\n")
    
    index += 1
        


