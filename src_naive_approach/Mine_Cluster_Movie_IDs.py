'''
Name        : Mine_Cluster_Movie_IDs.py
Version     : 1.0a
Author      : Alpaca


Input: Cluster Number from Dictionary generated by ___________________________
Output: Array of Movie ID & Ratings from combined_data*

Details:
1. The output is the ratings for all the movies watched by UserID as compiled in MovieIDDict.csv
2. This will be done by using the MovieID
'''

def Mine_Cluster_Movie_IDs(DesiredClusterNumber):
    # file name movieIDClusters dictionary generated by _____________________
    fileName = '../data/movieIDClusters.csv'
    # open the file
    FileHeader = open(fileName, 'r')

    count = 0
    # Read First Line
    line = FileHeader.readline()

    # Empty arrive for movie ID
    MovieIDs = []

    # Looping through the lines    "Movie Dictionary has the following format:
    # MovieID, Cluster \n
    while line:
        count += 1
        data = line.split(',')
        MovieClusterNumber = int(data[1].strip('\r').strip('\n').strip('\r').strip('\n'))
        if DesiredClusterNumber == MovieClusterNumber:
            MovieIDs.append(int(data[0]))
        # Read Next Line
        line = FileHeader.readline()

    FileHeader.close()
    return MovieIDs