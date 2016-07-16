# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.

results = [
        {'Austria': 0, 'Hungary': 2},
        {'Portugal': 1, 'Iceland': 1},
        {'Iceland': 1, 'Hungary': 1},
        {'Portugal': 0, 'Austria': 0},
        {'Iceland': 2, 'Austria': 1},
        {'Hungary': 3, 'Portugal': 3},
]

print('There were {} matches in the group'.format(len(results)))

# TODO: Write code to answer the following questions:

print('The match with the most goals was', '?')
print('The match with the fewest goals was', '?')
print('The team with the most total goals was', '?')
print('The team with the fewest total goals was', '?')
print('The team with the most points was', '?')
print('The team with the fewest points was', '?')

# TODO (extra): Write code to compute and display a league table
