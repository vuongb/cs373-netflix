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

import glob

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
    # Read in probeData.txt and get customers that have ratings for given movieIDs
    # Build a List of Lists where Outer list indicies == movieID and Inner list are customerIDs
    # aka adjacency list
    MOVIE_NUM       = 17770
    MovieCustArray  = [ []  for i in range(MOVIE_NUM + 1)]
    MovieOrder      = []
    movieID         = -1
    custID          = -1
    a               = []
    print "Reading from probeData.txt"
    inputFile = open("data/probeData.txt", "r")
    for line in inputFile :
        if line == "\n":
            break
        elif ":" in line :
            if movieID != -1 :
                MovieCustArray[movieID] = a
                a = []
            movieID = int(line.rstrip(':\n'))
            MovieOrder.append(movieID)
        else :
            custID = int(line.rstrip('\n'))
            a.append(custID)
    print "Done reading from probeData.txt"
    inputFile.close()
    print

    # Go through training data and get ratings by referencing customerID
    print "Parsing ratings from training data."
    MovieCustOutput = [ []  for i in range(MOVIE_NUM + 1)]
    movieID = -1
    custID = -1
    x = 0
    for f in glob.glob("../training_data/*.txt"):
        inputFile = open(f)
        print "parsing file " + str(x)
        x += 1
#        if x > 500:         # TODO: remove. Only used to test small dataset.
#            break
        for line in inputFile :
            if line == "\n" : # if EOF
                break
            elif ":" in line : # if line is a movieID
                movieID = int(line.rstrip(':\n'))
                if len(MovieCustArray[movieID]) == 0 : # means you don't care about the ratings for this movie
                    break
            else:   # else it's a customerID
                l = line.rstrip('\n').split(',')
                custID = int(l[0])
                custRating = int(l[1])
                if custID in MovieCustArray[movieID] :
                    tup = (custID, custRating)
                    MovieCustOutput[movieID].append(tup)
        inputFile.close()
    print "Done parsing training data."
    print

    # Write all movies and their customers and ratings to output file
    print "Writing output file."
    outputFile = open('data/probeCustomerandRatings.txt', 'w')
    for movieNum in MovieOrder :

            outputFile.write(str(movieNum) + ":\n") # write the movieID

            for customer in MovieCustArray[movieNum] :
                #tupleIndex = [x[0] for x in MovieCustOutput[movieNum]].index(custID)
                custRating = dict(MovieCustOutput[movieNum])[customer]
                outputFile.write(str(custRating) + "\n")


    outputFile.close()
    print "Done printing output."

movie_titles_dict = {}
def build_movie_titles_dict():
    global movie_titles_dict
    r = open('data/movie_titles.txt', 'r')
    while True:
        line = r.readline().rstrip('\n')
        if line == '':
            break
        else:
            data = line.split(',')
            movieID = int(data[0])
            if data[1] != 'NULL':       # Some movie years are null
                movieYear = int(data[1])    # doesn't account for multiple movie years, but there's not many of them so whatever
                movie_titles_dict[movieID] = movieYear
    r.close()
    return movie_titles_dict

decade_dict = {}
def build_decade_dict():
    global decade_dict
    x = 0
    decade = -1
    for file in glob.glob("../training_data/*.txt"):
        input = open(file)
        print "parsing file " + str(x)
        x += 1
        # if x > 10: # TODO: remove after testing
        #     break
        for line in input:
            if line == "\n":
                break
            elif ':' in line:   # if it's a movieID
                movieID = int(line.rstrip(':\n'))
                movieYear = movie_titles_dict.get(movieID)  # looks up year of movie from movie_titles_dict
                decade = get_year_index_helper(movieYear)
            else:   # else its a rating set
                data = line.rstrip('\n')
                data = data.split(",")  # [customerID, rating, ratingDate]
                customerID = int(data[0])
                rating = int(data[1])
                decade_list = decade_dict.get(customerID)
                if not decade_list:     # if the customer isn't in the dictionary, intitialize decade_list
                    decade_list = [ [0,0]  for i in range(11)]
                    decade_dict[customerID] = decade_list
                decade_list[decade][0] += rating        # cumulative sum
                decade_list[decade][1] += 1             # of ratings
        input.close()


def get_year_index_helper(movieYear):
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

    return result


def print_decade_dict():
    global decade_dict
    output = open("caches/customer_decade_rating.out", "w")
    for key in decade_dict.keys():
        decade_list = decade_dict.get(key)
        output_list = []
        index = 0
        for decade_data in decade_list:
            if decade_data[1] != 0:
                average = float(decade_data[0])/decade_data[1]
                output_list.append([index, average])
            index +=1
        if output_list != []:               # only print out the customers who have ratings, and only the decades they've rated int
            output.write( str(key) + ':\n')
            for data in output_list:
                output.write(str(data[0]) + ',' + str(data[1]) + '\n')
    output.close()


# ----
# main
# ----

#read_training_data_avgmovie()

#read_training_data_avgcust()

#build_probe_answers()

build_movie_titles_dict()
build_decade_dict()
print_decade_dict()
