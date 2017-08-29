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
    while True:

        rest_score = raw_input("Enter the score for this restaurant: ")

        try:
            if type(int(rest_score)) and int(rest_score) in range(1, 6):
                ratings[rest_name] = rest_score
                break
            else:
                print "Ratings must be a number between 1 and 5."
                continue
        except ValueError:
            print "Ratings must be a number between 1 and 5."
            continue

    print
    print "Thanks for your submission, here are the new restaurant ratings!"
    print
    print
    print_sorted_ratings(ratings)


create_ratings_dict(filename)

print "Welcome to this fabulous restaurant rating app"

while True:

    print
    print "You have two options:"
    print "1. See all current ratings"
    print "2. Add a new restaurant and rate it."
    choice = raw_input("What would you like to do? (1 or 2): ")

    if choice == "1":
        print_sorted_ratings(ratings)
        continue
    elif choice == "2":
        add_new_entry()
        print "What would you like to do next?"
        continue
    elif choice == "q":
        break

