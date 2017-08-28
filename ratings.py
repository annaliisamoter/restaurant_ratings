"""Restaurant rating lister."""


import sys

filename = sys.argv[1]

def create_ratings_dict(filename):
    """creates dictionary of restaurants and ratings from text file."""

    ratings = {}
    for line in open(filename):
        line = line.strip()
        line = line.split(":")

        for item in line:
            ratings[line[0]] = line[1]

    #rest_list = ratings.items()
    sorted_rests = sorted(ratings)
    for rest in sorted_rests:
        print "{} is rated at {}.".format(rest, ratings[rest])




create_ratings_dict(filename)