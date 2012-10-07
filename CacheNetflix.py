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

    
## ----
## AvgCustRating_Print
## ----
#def AvgCustRating_Print (w, custTotalArray, custNumArray):
#
#    """
#    loop through arrays, calculate average, write
#    w is a writer
#    custTotalArray is an array with the sums of all the ratings for a custID (array indexes are the custID - 1)
#    custNumArray is an array of the number of times a custID did a rating (array indexes are the custID - 1)
#    """
#    assert len(custTotalArray) == custNum
#    assert len(custNumArray) == custNum
#
#    # If custID hasn't rated anything, print anyways
#    for i in range(custNum) :
#
#        custID = i + 1
#
#        # Last Line Case
#        if i == custNum-1 :
#            w.write(str(custID) + "," + str(round(custTotalArray[i]/custNumArray[i])))
#        else:

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

# ----
# main
# ----

#read_training_data_avgmovie()

read_training_data_avgcust()

#AvgCustRating_Netflix(sys.stdin, sys.stdout)

