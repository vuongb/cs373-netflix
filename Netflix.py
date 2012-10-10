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

import math

def read_avg_movie_cache(input, size):
    movie_rating_cache      = [0]*size
    while True:
        data       = input.readline().strip('\n')# remove EOL characters
        if data == "":  # if EOF
            break
        else:
            data    = data.split(':')  #split into a data list
            movie_id    = int(data[0])
            movie_rating= int(data[1])
            movie_rating_cache[movie_id] = movie_rating     # Build our indexable cache
    
    return movie_rating_cache


def read_avg_customer_cache(input, size):
    customer_rating_cache   = [0]*size
    while True:
        data       = input.readline().strip('\n')# remove EOL characters
        if data == "":  # if EOF
            break
        else:
            data    = data.split(':')  #split into a data list
            customer_id = int(data[0])
            movie_rating= int(data[1])
            customer_rating_cache[customer_id] = movie_rating     # Build our indexable cache

    return customer_rating_cache



# Weights
# (customer:movie) - before extremity testing
    #  1 : 1 -> 1.1565250495
    #  2 : 1 -> 1.47431192534
    #  3 : 1 -> 2.86086310726
    #  4 : 1 -> 4.40117897681
    #  1 : 2 -> 1.44662779423
    #  1 : 3 -> 2.78770284902
    #  1 : 4 -> 4.28639893013
    #  0.25 : 1.00 -> 2.01165881019
    #  0.50 : 1.00 -> 1.70445882173
    #  0.75 : 1.00 -> 1.40371046471
    #  0.85 : 1.00 -> 1.27685076585
    #  0.93 : 1.00 -> 1.20643843618
    #  0.97 : 1.00 -> 1.17101711143
    #  1.00 : 0.25 -> 1.98429445923
    #  1.00 : 0.75 -> 1.39795340259
    #  1.00 : 0.93 -> 1.20626670786
    #  1.00 : 0.97 -> 1.16705817031
# Extremity margins (1:1) weight
    # 0.25 -> 1.15592131358
    # 0.50 -> 1.15598683409
    # 0.75 -> 1.15686153674
def compute_estimated_rating(avg_customer_rating, avg_movie_rating):
    if avg_customer_rating != 0 :

        # Cast to floats
        avg_customer_rating = float(avg_customer_rating)
        avg_movie_rating    = float(avg_movie_rating)

        # Weights
        customer_rating_weight  = 1.0
        movie_rating_weight     = 1.0

        # Extremities
        if avg_customer_rating < 2 or avg_customer_rating > 4:
            customer_rating_weight += 0.10   # Extremity margin
        if avg_movie_rating < 2 or avg_movie_rating > 4:
            movie_rating_weight += 0.10      # Extremity margin

        estimated_rating = ( (avg_customer_rating*customer_rating_weight) + (avg_movie_rating*movie_rating_weight) ) / 2    # Average the avg_cust_rating and avg_movie_rating (considering weights)

        return estimated_rating
    else :
        return avg_movie_rating                                     # If no average customer rating, then just give movie recommendation


def square_diff (x, y) :
    return (x - y) ** 2


# Main
def Netflix_solve(r, w) :
    CUSTNUM                 = 2649429
    MOVIENUM                = 17770

    input               = open("caches/avg_movie_rating.out", "r")
    avg_movie_cache     = read_avg_movie_cache(input, MOVIENUM + 1)
    input.close()

    input               = open("caches/avg_customer_rating.out", "r")
    avg_customer_cache  = read_avg_customer_cache(input, CUSTNUM + 1)
    input.close()

    movieID = -1

    #output = open('probeEstimated.txt', 'w')
    output = w

    #for line in open("data/probeData.txt", "r"):
    for line in r:
        if line == "\n" :
            break
        elif ":" in line :
            movieID = int(line.rstrip(':\n'))
            output.write(str(movieID) + ":\n")
        else :
            custID = int(line.rstrip('\n'))
#            print "customer rating  : " + str(avg_customer_cache[custID])
#            print "movie rating     : " + str(avg_movie_cache[movieID])
            estimated_rating = compute_estimated_rating(avg_customer_cache[custID], avg_movie_cache[movieID])
#            print "estimated rating : " + str(estimated_rating)
            s = "%.1f" % estimated_rating
            output.write(s + "\n")
    output.close()


