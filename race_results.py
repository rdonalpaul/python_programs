# Processing Race Results

Number_of_Finishers = 3

def ReadDictionary ( filename ) : #Reads in File, Entry List
    try :
        filehandle = open ( filename, "r" )
    except IOError :
        print ('File Cannot be Read')
        return
    dictionary = { }
    for line in filehandle :
        linewords = line.split( )
        dictionary [linewords[0]] = linewords[1], linewords[2]
    return dictionary


def Results ( filename ) :# Race Numbers are entered as they cross finish line
    points = 0          # All Results are placed in Dictionary - totalresults
    totalresults = {}
    TeamResults = {}
    TeamScores = {}
    FinalResults = {}
    report = 0
    entrylist = ReadDictionary ( filename )
    print ('Please Enter Race Number, 0 Exits Program')
    while True :
        result = str(input('Please Enter Race Number:')) #Enter Race Results
        if result ==  '0' :
            break
        elif result not in entrylist : 
            print ( 'This Entry id is Invalid!' ) # Print Error
        elif result in totalresults :
            print ( 'Result Already Entered!' ) # Print Error
        else :
            points += 1 # Calculates Points & Displayes \
                        # them in Dictionary, totalresults
            totalresults[result] = points, entrylist[result][0], \
                                   entrylist[result][1]
            if totalresults[result][2] not in TeamResults :
                color =  totalresults[result][2]
                TeamResults [totalresults[result][2]] \
                            =[totalresults[result][1] ] # Team Members
                TeamScores [totalresults[result][2]] = \
                           totalresults[result][0] # Positions
            else :
                TeamResults [totalresults[result][2]] += \
                            [totalresults[result][1]]  # Team Members
                TeamScores [totalresults[result][2]] += \
                           totalresults[result][0] # Positions
                color =  totalresults[result][2]
                if len(TeamResults[color]) == Number_of_Finishers :
                       print ('Score = %s Team =  %s: %s' % \
                              (TeamScores [totalresults[result][2]], \
                               totalresults[result][2], ", ".join\
                               (TeamResults[totalresults[result][2]])))
                  
            report += 1  
            FinalResults[color] = [TeamScores [totalresults[result][2]], \
                                   TeamResults [totalresults[result][2]], \
                                   report]
    FinalResults = sorted([[FinalResults[key][0], key, FinalResults[key][1]] \
                           for key in FinalResults])
    # Prints Final Table
    print ('%s %7s %8s %15s' % ( 'Place', 'Score', 'Team', 'Scoring Member'))
    loop = 1
    for item in FinalResults :
        if len(item[2]) >= Number_of_Finishers :
            print ("%2i %8i %11s %16s" % (loop, item[0], \
                                          item[1], ", ".join(item[2])))
            loop +=1
            
 
def RaceResults ( filename ) : # Final Function
    results = Results ( filename )

