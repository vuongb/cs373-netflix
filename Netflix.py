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


CUSTNUM                 = 2649429
MOVIENUM                = 17770
customer_rating_cache   = [0]*(CUSTNUM + 1)
movie_rating_cache      = [0]*(MOVIENUM + 1)


def read_avg_movie_cache():
    input           = open("caches/avg_movie_rating.out", "r")
    while True:
        data       = input.readline().strip('\n')# remove EOL characters
        if data == "":  # if EOF
            break
        else:
            data    = data.split(':')  #split into a data list
            movie_id    = int(data[0])
            movie_rating= int(data[1])
            movie_rating_cache[movie_id] = movie_rating     # Build our indexable cache
    print "Read movie cache."
    input.close()

def read_avg_customer_cache():
    input           = open("caches/avg_customer_rating.out", "r")
    x = 0
    while True:
        data       = input.readline().strip('\n')# remove EOL characters
        if data == "":  # if EOF
            break
        else:
            data    = data.split(':')  #split into a data list
            customer_id = int(data[0])
            movie_rating= int(data[1])
            customer_rating_cache[customer_id] = movie_rating     # Build our indexable cache
        print x
        x +=1
    print "Read customer cache."
    input.close()

def compute_estimated_rating(avg_customer_rating, avg_movie_rating):
    return ((avg_customer_rating*1.0) + avg_movie_rating)/2     # Average the avg_cust_rating and avg_movie_rating (formatted to float)

#def print_output():


# Main


read_avg_customer_cache()
read_avg_movie_cache()

movieID = -1
custID = -1


output = open('probeEstimated.txt', 'w')

for line in open("data/probeData.txt", "r"):
    if line == "\n" :
        break
    elif ":" in line :
        movieID = int(line.rstrip(':\n'))
        output.write(str(movieID) + ":\n")
    else :
        custID = int(line.rstrip('\n'))
        estimated_rating = compute_estimated_rating(customer_rating_cache[custID], movie_rating_cache[movieID])
        s = "%.1f" % estimated_rating
        output.write(s + "\n")
#rmse = computeRmse(open("data/probeAnswers.txt"), ratings)


#print_output()