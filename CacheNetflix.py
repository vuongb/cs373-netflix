#!/usr/bin/env python

# ---------------------------
# Name  : Ryan J. Prater
#       : Bryan Vuong
# EID   : rp22566
#       : bkv85
# CSID  : rprater
#       :
# CS373 - Downing - Project #3 - Netflix
# ---------------------------

"""
To run the program
    % python CacheNetflix.py < <>.txt > <>.txt
    % chmod ugo+x RunNetflix.py
    % CacheNetflix.py < <>.txt > <>.txt
"""

import sys

custNum = 2649429
custTotalArray = [0] * custNum
custNumArray = [0] * custNum


# ----
# AvgCustRating_Netflix
# ----
"""
    AvgCustRating should be passed the Training
    Set file and computes the avg rating for
    every customer_id
"""

def avg_customer_rating(input) :
    """ 
    read loop, eval, print
    """
    global custTotalArray
    global custNumArray
    assert custNum > 0
    

    
    # Loop through every line in r:
    #   Add the rating on each line to custTotalArray for each custID
    #   Add 1 for every rating read for a custID
    a = []
    input.readline()        # iterate over the movie id, we don't need it.
    while cache_read(input, a):
        custIDIndex = int(a[0]) - 1
        custTotalArray[custIDIndex] += int(a[1])
        custNumArray[custIDIndex] += 1
        a = []

# ----
# cache_read
# ----
    """
    reads ints into a
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """

def cache_read (input, a):
    s = input.readline()
    if s == "":
        return False
    l = s.split(",")
    a.append(l[0])
    a.append(l[1])
    return True


def avg_movie_rating(input):
#    input           = open("data/mv_0002043.txt", "r")
    num_ratings     = 0
    total_points    = 0
    line            = input.readline()
    line            = line.rstrip('\n')
    movie_id        = line
    single_rating   = []
    result          = {}
    result['movie_id'] = movie_id

    while True:
        line            = input.readline()
        line.strip('\n')
        if line == "":
            break
        single_rating   = line.split(",")       # Split and get [customer_id, rating, rating_date]
        num_ratings     += 1                    # Get the # of ratings so we can take an average
        total_points    += int(single_rating[1])     # Add the ratings together

    avg_movie_rating = total_points/num_ratings
    input.close()
    result['avg_rating']    = avg_movie_rating
    return result



def read_training_data_avgmovie():
    import glob
    output = open("avg_movie_rating.out","w")
    x = 0
    for f in glob.glob("../training_data/*.txt"):
        input = open(f)
        result = avg_movie_rating(input)
        input.close()
        output.write(result['movie_id'] + str(result['avg_rating']) + "\n")          # write movieid
        print x
        x += 1
    output.close()

def read_training_data_avgcust():
    import glob
    x = 0
    for f in glob.glob("../training_data/*.txt"):
        input = open(f)
        avg_customer_rating(input)
        input.close()
        print x
        x += 1

    output = open("avg_customer_rating.out","w")
    for i in range(custNum):
        custID = i+1
        if custNumArray[i] != 0:
            output.write(str(custID) + ":" + str(int(round(custTotalArray[i]/custNumArray[i]))) + "\n")
        print i
    output.close()

def build_probe_answers():

    MOVIE_NUM = 17770
    CUST_NUM = 480189
    
    import glob
    MovieCustArray = [ [] ] * (MOVIE_NUM + 1)
    outputFile = open('probeEstimated.txt', 'w')
    inputFile = open("data/probeData.txt", "r")

    movieID = -1
    custID = -1
    a = []

    # Read in each line
    # Build a List of Lists
    # Every element of the Outer List, is an Inner List of the CustIDs for every MovieID
    for line in open(inputFile):
        if line == "\n":
            break
        elif ":" in line :
            movieID = int(line.rstrip(':\n'))
            if len(a) != 0 :
                MovieCustArray[movieID] = a
                a = []
        else :
            custID = int(line.rstrip('\n'))
            a.append(custID)
    if len(a) != 0 :
        MovieCustArray[movieID] = a

    inputFile.close()
    
    # Go through training data and get ratings
    MovieCustOutput = [ [] ] * (MOVIE_NUM + 1)
    movieID = -1
    custID = -1
    for f in glob.glob("../training_data/*.txt"):
        inputFile = open(f)
        for line in open(inputFile) :
            if line == "\n" :
                break
            elif ":" in line :
                movieID = int(input.readline().rstrip(':\n'))
                if len(MovieCustArray[movieID]) == 0 :      # means you don't care about the ratings for this movie
                    break
            else:
                l = line.rstrip('\n').split(',')
                custID = l[0]
                custRating = l[1]
                if custID in MovieCustArray[movieID] :
                    tup = (custID, custRating)
                    MovieCustOutput[movieID].append(tup)
        f.close()

    # Write all movies and their customers and ratings to output file
    for movieNum in range(1, (MOVIE_NUM + 1)) :
        if len(MovieCustOutput[movieNum]) != 0 :
            outputFile.write(str(movieNum) + "\n")
            for u,v in MovieCustOutput[movieNum] :
                outputFile.write(str(v) + "\n")
            
    

    outputFile.close()
##    output = open("caches/probeAnswers.txt","w")
##    x = 0
##    for f in glob.glob("../training_data/*.txt"):
##        input = open(f)
##        movie_id = input.readline()
##        if movie_id:
##            output.write(movie_id)
##            while True:
##                values = input.readline().split(",")
##                if values == ['']:
##                    break
##                customer_rating = values[1]
##                output.write(customer_rating + "\n")          # write movieid and ratings for each cust
##        input.close()
##        print x
##        x += 1
##    output.close()

# ----
# main
# ----

#read_training_data_avgmovie()
#read_training_data_avgcust()
build_probe_answers()
