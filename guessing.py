def FindNumber():
    #Pick a number and the program will guess your number in the least
    #amount of attemtps as possible. Only '<', '>' or '=' can be used.
    lo = 0
    hi = 2
    print("Input '<' if my guess is smaller,  Input '>' if my guess is greater")
    print("or input '=' if guess is correct")
    hinum = False
    count = 0
    while lo < hi:
        mid = ( lo + hi )//2
        print(mid)
        response = str(input("Please enter < or > or = :  "))
        if response == '=' :
            count += 1
            break
        elif response == '<' :
            hinum = True
            print('I will guess a smaller number')
            count += 1
            hi = mid - 1
        elif response == '>' :
            print('I will guess a bigger number')
            count += 1
            lo = mid + 1
            if hinum == False:
                hi = hi*2
        else:
            print('Please use < > or = ')
    print('Number is: ',(lo + hi ) // 2)
    print('Number of Guesses: %s' % count)
        
            
    
