"""Restaurant rating lister."""


import sys

filename = sys.argv[1]

ratings = {}


def create_ratings_dict(filename):
    """creates dictionary of restaurants and ratings from text file."""

    for line in open(filename):
        line = line.strip()
        line = line.split(":")

        for item in line:
            ratings[line[0]] = line[1]

    return ratings


def print_sorted_ratings(ratings):
    """ prints a sorted read out of restaurants and ratings from a dictionary"""

    sorted_rests = sorted(ratings)
    for rest in sorted_rests:
        print "{} is rated at {}.".format(rest, ratings[rest])


def add_new_entry():
    """ prompts user to add new entry to ratings dictionary """

    print
    rest_name = raw_input("Enter the restaurant do you want to rate: ")
    print
    rest_score = raw_input("Enter the score for this restaurant: ")

    ratings[rest_name] = rest_score

    print
    print "Thanks for your submission, here are the new restaurant ratings!"
    print
    print
    print_sorted_ratings(ratings)


print_sorted_ratings(create_ratings_dict(filename))

add_new_entry()
