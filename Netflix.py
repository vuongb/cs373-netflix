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


def read_avg_movie_cache(input, size):
    """
    input is the movie cache file
    size is the number of movies
    builds a cache of avg ratings per movie
    returns a list of average movie ratings where the movie IDs are indexes
    """

    assert size > 0

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
    """
    input is the customer cache file
    size is the number of customers
    builds a cache of avg ratings per customer
    returns a list of average customer ratings where the customer IDs are indexes
    """
    assert size > 0

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


def read_decade_cache(input):
    """
    input is the decade cache file
    builds a cache of avg customer ratings per decade
    returns a dictionary of customer ratings (keys) and rating lists (values)
    """

    decade_dict = {}
    customerID  = -1
    while True:
        data = input.readline()
        if data == "\n" or data == '':
            break
        elif ':' in data:
            customerID = int(data.rstrip(":\n"))
        else:
            assert customerID > 0

            data = data.rstrip('\n')
            average_list = data.split(',')
            decade_list = decade_dict.get(customerID)
            if not decade_list:                             # if the customer isn't in the dictionary, intitialize decade_list
                decade_list = [ 0  for i in range(11)]
                decade_dict[customerID] = decade_list
            decade_list[int(average_list[0])] = float(average_list[1])
    return decade_dict


def build_movie_titles_dict(input):
    """
    input is the movie title decade cache file
    builds a cache of what decade each movie was in
    returns a dictionary of movieIDs (keys) and movieYears (values)
    """

    movie_titles_dict = {}
    while True:
        line = input.readline().rstrip('\n')
        if line == '':
            break
        else:
            data = line.split(',')
            movieID = int(data[0])

            assert movieID > 0

            if data[1] != 'NULL':       # Some movie years are null
                movieYear = int(data[1])    # doesn't account for multiple movie years, but there's not many of them so whatever
                movie_titles_dict[movieID] = movieYear
    input.close()
    return movie_titles_dict

def get_year_index_helper(movieYear):
    """
    movieYear is the year the movie was released
    returns the index in decade_dict where the movie is cached
    """

    result = -1
    if movieYear < 1909:
        result = 0
    elif movieYear >= 1910 and movieYear <= 1919:
        result = 1
    elif movieYear >= 1920 and movieYear <= 1929:
        result = 2
    elif movieYear >= 1930 and movieYear <= 1939:
        result = 3
    elif movieYear >= 1940 and movieYear <= 1949:
        result = 4
    elif movieYear >= 1950 and movieYear <= 1959:
        result = 5
    elif movieYear >= 1960 and movieYear <= 1969:
        result = 6
    elif movieYear >= 1970 and movieYear <= 1979:
        result = 7
    elif movieYear >= 1980 and movieYear <= 1989:
        result = 8
    elif movieYear >= 1990 and movieYear <= 1999:
        result = 9
    elif movieYear >= 2000:
        result = 10

    if result == -1:        # TODO: better error handling, hopefully this never happens
        result = 0

    assert result >= 0

    return result


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
# Only using movie decade cache if there's a value:
    # 1.00027210964
# Averaging them all together:
    # 1.05768547027
# Weights (customer:movie:decade)
    # 30:20:50 = 1.02742536532
    # 20:20:60 = 1.00980631617
    # 15:15:70 = 1.00043221784
    # 10:10:80 = 0.995471917655
    #  8: 8:84 = 0.994889654135
    #  5: 5:90 = 0.995487209784
def compute_estimated_rating(avg_customer_rating, avg_movie_rating, decade_rating):
    """
    avg_customer_rating is the customer's average rating
    avg_movie_rating is the movie's average rating
    decade_rating is the customer's average decade rating (highest weight)
    returns the algorithm's estimated rating based on weights
    """


    assert avg_customer_rating >= 0
    assert avg_movie_rating >= 0
    assert decade_rating >= 0

    avg_customer_rating = float(avg_customer_rating)
    avg_movie_rating    = float(avg_movie_rating)

    # Weights (make sure they add to 100 and then divide by 100)
    if avg_customer_rating == 0:
        customer_rating_weight = 0
    else:
        customer_rating_weight  = 8

    if avg_movie_rating == 0:
        movie_rating_weight = 0
    else:
        movie_rating_weight = 8
    if decade_rating == 0:
            decade_rating_weight = 0
    else:
        decade_rating_weight = 84

    total_weight            = customer_rating_weight + movie_rating_weight + decade_rating_weight

    if total_weight == 0:
        return 0.0
#
#        # Extremities
#        if avg_customer_rating < 2 or avg_customer_rating > 4:
#            customer_rating_weight += 0.10   # Extremity margin
#        if avg_movie_rating < 2 or avg_movie_rating > 4:
#            movie_rating_weight += 0.10      # Extremity margin

    estimated_rating = ( (avg_customer_rating*customer_rating_weight) + (avg_movie_rating*movie_rating_weight) + (decade_rating*decade_rating_weight) ) / total_weight

    assert estimated_rating >= 0.0

    return estimated_rating

def square_diff (x, y) :
    """
    x is a real number
    y is a real number
    returns the square difference between x and y
    """

    return (x - y) ** 2



CUSTNUM                 = 2649429
MOVIENUM                = 17770
def Netflix_solve(r, w) :
    """
    r is a stdin file that specifies the movieIDs and custIDs ratings that are requested
    w is a stdout file for where the recommended ratings are printed
    Gives recommended ratings for movieIDs and custIDs specified in r
    """

    input               = open('data/movie_titles.txt', 'r')
    movie_titles_dict   = build_movie_titles_dict(input)
    input.close()

    input               = open("caches/customer_decade_rating.out", "r")
    decade_cache        = read_decade_cache(input)
    input.close()

    input               = open("caches/avg_movie_rating.out", "r")
    avg_movie_cache     = read_avg_movie_cache(input, MOVIENUM + 1)
    input.close()

    input               = open("caches/avg_customer_rating.out", "r")
    avg_customer_cache  = read_avg_customer_cache(input, CUSTNUM + 1)
    input.close()



    output = w
    while True:
        movieID     = -1
        movieDecade = -1
        line = r.readline()
        while line and line != "\n":    # while it's not the EOF and not EOL
            if ":" in line :
                movieID     = int(line.rstrip(':\n'))

                assert movieID > 0

                movieDecade = movie_titles_dict.get(movieID)
                output.write(str(movieID) + ":\n")
            else :
                custID              = int(line.rstrip('\n'))

                assert custID > 0

                decade_rating       = (decade_cache.get(custID))[get_year_index_helper(movieDecade)]    # get the average customer rating for the index corresponding to the decade
                estimated_rating    = compute_estimated_rating(avg_customer_cache[custID], avg_movie_cache[movieID], decade_rating)

                s                   = "%.1f" % estimated_rating
                output.write(s + "\n")
            line = r.readline()
        if line == "\n":        # separate individual tests with blank lines
            output.write("\n")
        if not line:            # check for EOF
            break


