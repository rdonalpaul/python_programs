import random

def TotalScore(dice):
    # The sum of the scores obtained by rolling ‘dice’ 
    return sum(random.randint(1, 6) for i in range(dice))
    


def Percent(part, whole):
    # The percentage which the integer ‘part’forms of the integer ‘whole’,
    # rounded to the closest integer
    total = (part/whole)*100
    return round(total)


def DiceRolls():
    # Simulates rolling a given number of dice for a given number of rolls
    # and showing the percentage of the total and a histogram of the
    # percentage of times each score is obtained
    while True:
        diceNum = int(input("Please enter the number of dice:"))
        if diceNum == 0:
            print("Goodbye")
            break
        rolls = int(input("How many times would you like to roll the dice?:"))
        score = []
        for i in range(rolls):
            score.append(TotalScore(diceNum))
        for x in range(diceNum, diceNum*6+1):
            percentage = Percent(score.count(x), rolls)
            s1 = "%2s" % x
            s2 = "%2s" % percentage
            print(s1 + ":" + s2 + "%" +("*" * percentage))
        
            
