# Build a dictionary of movies and their voting customers
movieDict   = {}
movieID     = -1
input       = open("data/probeData.txt")
while True:
    line = input.readline()
    if line == "":
        break
    elif ":" in line:   # Add the movie to the dictionary
        movieID = int(line.rstrip(":\n"))
        movieDict[movieID] = []
    else:               # Add the customer to the list already in the dictionary
        customerID      = int(line.rstrip("\n"))
        customer_list   = movieDict.get(movieID)
        customer_list.append(customerID)
input.close()



# Choose random movies and make sure we have 1000 lines of output
import random
num_lines_output    = 0
output              = open("RunNetflix.in", "w")
while num_lines_output < 1000:
    random_movie = random.choice(movieDict.keys())  # Get a random movie from the dictionary
    num_lines_output += 1
    output.write(str(random_movie) + ":\n")
    for customer in movieDict.get(random_movie):    # Print out the customers who rated this movie
        output.write(str(customer) + "\n")
        num_lines_output += 1
    output.write("\n")
output.close()