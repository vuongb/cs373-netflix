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
customer_rating_cache   = [0]*CUSTNUM + 1
movie_rating_cache      = [0]*MOVIENUM + 1


def read_avg_movie_cache():
    input           = open("avg_movie_rating.out", "r")
    while True:
        data        = input.readline().rstrip('\n').split(":")  # remove EOL characters and split into a data list
        if data == "":  # if EOF
            break
        movie_id    = int(data[0])
        movie_rating= int(data[1])
        movie_rating_cache[movie_id] = movie_rating     # Build our indexable cache
    input.close()

def read_avg_customer_cache():
    input           = open("avg_customer_rating.out", "r")
    while True:
        data        = input.readline().rstrip('\n').split(":")  # remove EOL characters and split into a data list
        if data == "":  # if EOF
            break
        customer_id = int(data[0])
        movie_rating= int(data[1])
        movie_rating_cache[customer_id] = movie_rating     # Build our indexable cache
    input.close()

def compute_estimated_rating(avg_customer_rating, avg_movie_rating):
    return ((avg_customer_rating*1.0) + avg_movie_rating)/2     # Average the avg_cust_rating and avg_movie_rating (formatted to float)

def compute_rmse():

def print_output():


# Main


read_avg_customer_cache()
read_avg_movie_cache()

# read in movie id
    #read in cust_id
    #compute estimated
    #compute

    compute_estimated_rating(avg_customer_rating, avg_movie_rating)
compute_rmse()
print_output()