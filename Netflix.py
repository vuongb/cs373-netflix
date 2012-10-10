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

def compute_estimated_rating(avg_customer_rating, avg_movie_rating):
    return ((avg_customer_rating*1.0) + avg_movie_rating)/2     # Average the avg_cust_rating and avg_movie_rating (formatted to float)


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

            print "customer rating  : " + str(avg_customer_cache[custID])
            print "movie rating     : " + str(avg_movie_cache[movieID])
            estimated_rating = compute_estimated_rating(avg_customer_cache[custID], avg_movie_cache[movieID])
            print "estimated rating : " + str(estimated_rating)
            print 
            s = "%.1f" % estimated_rating
            output.write(s + "\n")
    output.close()






