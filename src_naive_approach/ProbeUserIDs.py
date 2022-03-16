def ProbeMovieRatings(MovieID):

    fileHeader = open("../data/probe.txt", 'r')
    AllLines = fileHeader.readlines()
    counter = 0
    for currentLine in AllLines:
        if ':' in currentLine:
            a = ''
            for x in currentLine:
                if x != ':':
                    a = a + x
                else:
                    break
                if MovieID == a:
                    w = 1
                    userIDs = []
                    while w > 0 :
                        if ':' not in AllLines[counter+w]:
                            newline = AllLines[counter+w].strip('\n')
                            userIDs.append(newline)
                            w = w + 1
                        else:
                            continue
        counter = counter + 1

    return userIDs

# Test function

if __name__ == "__main__":
    pass
    # print(Mine_Cluster_Movie_IDs(0))
    # print(Mine_Dict_Movie_Ratings(1))