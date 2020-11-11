# PROGRAM SUMMARY
# This program is a basic script that takes the numbers collected from the Associate Press
# Poll results and calculates who wins each state, including congressional districts.
# The program uses for loops to determine the electoral winner of each state and
# then determines the winner of the election.

# Note: Popular vote numbers last updated Monday, November 9th, 2020 at 1700 PDT.

# import numpy as np

# Data points are separated into separate scripts:
from BidenVotes import biden_votes_array
from BidenVotes import biden_votes_cd_ME_array
from BidenVotes import biden_votes_cd_NE_array

from RecountMarginsPercentages import recount_margin_percentage_states_array
from RecountMarginsVotes import recount_margin_votes_states_array

from ElectoralVotes import electoral_votes_states_array
from ElectoralVotes import electoral_votes_cd_ME_array
from ElectoralVotes import electoral_votes_cd_NE_array
from ElectoralVotes import total_electoral_votes

from IndependentVotes import independent_votes_array
from IndependentVotes import independent_votes_cd_ME_array
from IndependentVotes import independent_votes_cd_NE_array

from ContestIndices import *
from ContestNames import *

from TrumpVotes import trump_votes_array
from TrumpVotes import trump_votes_cd_ME_array
from TrumpVotes import trump_votes_cd_NE_array


# Initialization of vote counts and counters:
biden_popular_votes = 0
trump_popular_votes = 0
independent_popular_votes = 0
total_popular_votes = 0

biden_electoral_votes = 0
trump_electoral_votes = 0
independent_electoral_votes = 0
cumulative_electoral_votes = 0

biden_contests_won = 0
trump_contests_won = 0
independent_contests_won = 0

biden_percentage_array = []
trump_percentage_array = []
independent_percentage_array = []

total_votes_array = []
state_recount_array = []

contest_number = 1
recount_counter = 0
total_contests = 51
district_analyzed_ME = 0
district_analyzed_NE = 0
winner_message = "WINNER"

presidential_index_biden = "Biden"
presidential_index_trump = "Trump"
presidential_index_independent = "Independent"

presidential_candidates = [presidential_index_biden, presidential_index_trump, presidential_index_independent]

popular_vote_arrays = []
popular_votes_cd_ME_arrays = []
popular_votes_cd_NE_arrays = []

for state in range(len(biden_votes_array)):
    popular_vote_arrays.insert(state, [biden_votes_array[state], trump_votes_array[state], independent_votes_array[state]])

for district in range(len(biden_votes_cd_ME_array)):
    popular_votes_cd_ME_arrays.insert(district, [biden_votes_cd_ME_array[district], trump_votes_cd_ME_array[district], independent_votes_cd_ME_array[district]])

for district in range(len(biden_votes_cd_NE_array)):
    popular_votes_cd_NE_arrays.insert(district, [biden_votes_cd_NE_array[district], trump_votes_cd_NE_array[district], independent_votes_cd_NE_array[district]])


#*****************************************A*N*A*L*Y*S*I*S*****************************************

electoral_vote_threshold = total_electoral_votes // 2 + 1

print("-" * 120)
print("-" * 120)
print("{:*^120}".format("E*L*E*C*T*I*O*N***T*I*M*E"))
print("-" * 120)
print("-" * 120)

print("There are {0} electoral votes up for grabs!".format(total_electoral_votes))
print("Each candidate must secure {0} electoral votes to win the presidential election.".format(electoral_vote_threshold))
print("In the event of a tie on the electoral vote, it will be up to Congress to decide.  Good luck!\n")

# input(print("Hit Enter To Continue"))

# This section of code ensures that I've entered different numbers for each candidate in each state:
for state in range(len(biden_votes_array)):
    if biden_votes_array[state] == trump_votes_array[state]:
        print("{0} have the same numbers and need their votes checked again!".format(states_array[state]))

differential_votes_array = []
differential_percentage_array = []

for state in range(len(biden_votes_array)):
    total_votes_array.insert(state, biden_votes_array[state] + trump_votes_array[state] + independent_votes_array[state])
    differential_votes_array.insert(state, abs(biden_votes_array[state] - trump_votes_array[state]))

    biden_percentage_array.insert(state, biden_votes_array[state] / total_votes_array[state])
    trump_percentage_array.insert(state, trump_votes_array[state] / total_votes_array[state])
    independent_percentage_array.insert(state, independent_votes_array[state] / total_votes_array[state])

    differential_percentage_array.insert(state, abs(biden_percentage_array[state] - trump_percentage_array[state]))

# This section is important to determine who won each state and tally up their electoral vote counts:
for state in range(len(electoral_votes_states_array)):

    # Adds votes in new state in analysis to running totals:
    biden_popular_votes += biden_votes_array[state]
    trump_popular_votes += trump_votes_array[state]
    independent_popular_votes += independent_votes_array[state]
    total_popular_votes += total_votes_array[state]

    cumulative_electoral_votes += electoral_votes_states_array[state]

    biden_popular_percentage = biden_popular_votes / total_popular_votes
    trump_popular_percentage = trump_popular_votes / total_popular_votes
    independent_popular_percentage = independent_popular_votes / total_popular_votes

    biden_contest_status = ""
    trump_contest_status = ""
    independent_contest_status = ""

    # Checks to see who received the most popular votes and awards them in electoral votes:
    winning_index = popular_vote_arrays[state].index(max(popular_vote_arrays[state]))
    contest_winner = presidential_candidates[winning_index]

    if contest_winner == presidential_index_biden:
        biden_electoral_votes += electoral_votes_states_array[state]
        biden_contests_won += 1
        biden_contest_status = winner_message
    elif contest_winner == presidential_index_trump:
        trump_electoral_votes += electoral_votes_states_array[state]
        trump_contests_won += 1
        trump_contest_status = winner_message
    else:
        independent_electoral_votes += electoral_votes_states_array[state]
        independent_contests_won += 1
        independent_contest_status = winner_message

    print("*" * 120)
    print("{:*^120}".format("Contest #{0} - Popular Vote Count for {1}:".format(contest_number, states_array[state])))
    print("*" * 120)

    print("-" * 120)
    print("{:<20s}{:<20s}{:<20s}{:<20s}".format('CANDIDATE', 'POPULAR VOTES', 'PERCENTAGE',
                                                'STATUS'))
    print("-" * 120)
    print("{:<20s}{:<20,d}{:<20.2%}{:<20s}".format('Biden', biden_votes_array[state], biden_percentage_array[state],
                                                   biden_contest_status))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20s}".format('Trump', trump_votes_array[state], trump_percentage_array[state],
                                                   trump_contest_status))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20s}".format('Independent', independent_votes_array[state], independent_percentage_array[state],
                                                   independent_contest_status))
    print("{:<20s}{:<20,d}{:<20.2%}".format('TOTAL', total_votes_array[state], 1))
    print("\n")

    # Checks to see if state has independent congressional districts:
    if state == array_index_ME:
        print("{:*^68}".format("CONGRESSIONAL***DISTRICT***CONTESTS"))
        for district_array in popular_votes_cd_ME_arrays:

            highest_vote_count = max(district_array)
            winning_index = district_array.index(highest_vote_count)
            district_winner = presidential_candidates[winning_index]

            if district_winner == presidential_index_biden:
                biden_electoral_votes += electoral_votes_cd_ME_array[district_analyzed_ME]
                biden_contests_won += 1
            elif district_winner == presidential_index_trump:
                trump_electoral_votes += electoral_votes_cd_ME_array[district_analyzed_ME]
                trump_contests_won += 1
            else:
                independent_electoral_votes += electoral_votes_cd_ME_array[district_analyzed_ME]
                independent_contests_won += 1
            print("{0} wins an electoral vote from {1}!".format(district_winner, congressional_district_ME_array[district_analyzed_ME]))
            district_analyzed_ME += 1
    elif state == array_index_NE:
        print("{:*^68}".format("CONGRESSIONAL***DISTRICT***CONTESTS"))
        for district_array in popular_votes_cd_NE_arrays:

            highest_vote_count = max(district_array)
            winning_index = district_array.index(highest_vote_count)
            district_winner = presidential_candidates[winning_index]

            if district_winner == presidential_index_biden:
                biden_electoral_votes += electoral_votes_cd_NE_array[district_analyzed_NE]
                biden_contests_won += 1
            elif district_winner == presidential_index_trump:
                trump_electoral_votes += electoral_votes_cd_NE_array[district_analyzed_NE]
                trump_contests_won += 1
            else:
                independent_electoral_votes += electoral_votes_cd_NE_array[district_analyzed_NE]
                independent_contests_won += 1
            print("{0} wins an electoral vote from {1}!".format(district_winner, congressional_district_NE_array[district_analyzed_NE]))
            district_analyzed_NE += 1
        print("")
    else:
        pass

    print("{0} wins {1} Electoral Votes from {2}!".format(contest_winner, electoral_votes_states_array[state], states_array[state]))
    print("Margin of Winning: {:,} Popular Votes, or {:.2%}".format(differential_votes_array[state], differential_percentage_array[state]))
    if state == array_index_MI:
        if differential_votes_array[state] <= recount_margin_votes_states_array[state]:
            print("The victory is within the threshold of {:,} votes and is eligible for recount!".format(recount_margin_votes_states_array[state]))
        else:
            print("The victory is beyond the threshold of {:,} votes and is not eligible for recount.".format(recount_margin_votes_states_array[state]))
    else:
        if recount_margin_percentage_states_array[state] == 0:
            print("This state does not engage in recount requests.")
        elif differential_percentage_array[state] < recount_margin_percentage_states_array[state] and recount_margin_percentage_states_array[state] < 1:
            print("The victory is within a threshold of {:.2%} and is eligible for a recount!".format(recount_margin_percentage_states_array[state]))
            state_recount_array.insert(recount_counter, states_array[state])
            recount_counter += 1
        elif recount_margin_percentage_states_array[state] != 1:
            print("The victory is beyond the threshold of {:.2%} and is not eligible for recount.".format(recount_margin_percentage_states_array[state]))
        else:
            print("Any candidate may request a recount.")

    biden_electoral_percentage = biden_electoral_votes / cumulative_electoral_votes
    trump_electoral_percentage = trump_electoral_votes / cumulative_electoral_votes
    independent_electoral_percentage = independent_electoral_votes / cumulative_electoral_votes

    print("\n")
    print("{:+^120}".format("ELECTORAL & POPULAR VOTE COUNT UPDATE"))
    print("\n" + "-" * 120)
    print("{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format('CANDIDATE', 'POPULAR VOTES', 'PERCENTAGE',
                                                       'ELECTORAL VOTES', 'PERCENTAGE'))
    print("-" * 120)
    print("{:<20s}{:<20,d}{:<20.2%}{:<20,d}{:<20.2%}".format('Biden', biden_popular_votes, biden_popular_percentage,
                                                        biden_electoral_votes, biden_electoral_percentage))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20,d}{:<20.2%}".format('Trump', trump_popular_votes, trump_popular_percentage,
                                                        trump_electoral_votes, trump_electoral_percentage))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20,d}{:<20.2%}".format('Independent', independent_popular_votes, independent_popular_percentage,
                                                       independent_electoral_votes, independent_electoral_percentage))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20,d}{:<20.2%}".format('TOTAL', total_popular_votes, 1, cumulative_electoral_votes, 1))

    contests_remaining = total_contests - contest_number
    print("\n Election contests remaining: {0}\n".format(contests_remaining))

    contest_number += 1

# Once all contests are accounted for, it's time to determine a winner and gain insights!
print("\n\n\n\n")
print("*" * 120)
print("{:*^120}".format("E*L*E*C*T*I*O*N***R*E*S*U*L*T*S"))
print("*" * 120 + "\n")

print("The election is over and the results are in...")

if biden_electoral_votes > trump_electoral_votes:
    winner = "Joe Biden"
    winning_electoral_votes = biden_electoral_votes
elif trump_electoral_votes > biden_electoral_votes:
    winner = "Donald Trump"
    winning_electoral_votes = trump_electoral_votes
else:
    winner = "yet to be determined by Congress!"
    winning_electoral_votes = total_electoral_votes / 2

# The election results are produced as such:
def election_results(biden_electoral_votes, trump_electoral_votes):
    print("The winner with {0} electoral votes is {1}!".format(winning_electoral_votes, winner))
    print("\n" + "{:*^120}".format("F*I*N*A*L***R*E*S*U*L*T*S"))
    print("-" * 120)
    print("{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}".format('CANDIDATE', 'POPULAR VOTES', 'PERCENTAGE',
                                                       'ELECTORAL VOTES', 'PERCENTAGE', 'CONTESTS WON'))
    print("-" * 120)
    print("{:<20s}{:<20,d}{:<20.2%}{:<20d}{:<20.2%}{:<20d}".format('Biden', biden_popular_votes, biden_popular_percentage,
                                                            biden_electoral_votes, biden_electoral_percentage, biden_contests_won))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20d}{:<20.2%}{:<20d}".format('Trump', trump_popular_votes, trump_popular_percentage,
                                                            trump_electoral_votes, trump_electoral_percentage, trump_contests_won))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20d}{:<20.2%}{:<20d}".format('Independent', independent_popular_votes, independent_popular_percentage,
                                                            independent_electoral_votes, independent_electoral_percentage, independent_contests_won))
    print("{:<20s}{:<20,d}{:<20.2%}{:<20d}{:<20.2%}".format('TOTAL', total_popular_votes, 1, cumulative_electoral_votes, 1))

election_results(biden_electoral_votes, trump_electoral_votes)


if len(state_recount_array) > 0:
    print("\nThere were {0} contests that were eligible for recounts:".format(recount_counter))
    for state in state_recount_array:
        print("\t - " + state)
else:
    print("\nNo contests were within the margins of recounting.")


# Insights of Data:
state_highest_independent_voters = states_array[independent_votes_array.index(max(independent_votes_array))]
state_highest_independent_percentage = states_array[independent_percentage_array.index(max(independent_percentage_array))]

state_lowest_independent_voters = states_array[independent_votes_array.index(min(independent_votes_array))]
state_lowest_independent_percentage = states_array[independent_percentage_array.index(min(independent_percentage_array))]

state_highest_biden_voters = states_array[biden_votes_array.index(max(biden_votes_array))]
state_highest_biden_percentage = states_array[biden_percentage_array.index(max(biden_percentage_array))]

state_lowest_biden_voters = states_array[biden_votes_array.index(min(biden_votes_array))]
state_lowest_biden_percentage = states_array[biden_percentage_array.index(min(biden_percentage_array))]

state_highest_trump_voters = states_array[trump_votes_array.index(max(trump_votes_array))]
state_highest_trump_percentage = states_array[trump_percentage_array.index(max(trump_percentage_array))]

state_lowest_trump_voters = states_array[trump_votes_array.index(min(trump_votes_array))]
state_lowest_trump_percentage = states_array[trump_percentage_array.index(min(trump_percentage_array))]

# Numbers Behind The Insights
highest_independent_voters = independent_votes_array[independent_votes_array.index(max(independent_votes_array))]
highest_independent_percentage = independent_percentage_array[independent_percentage_array.index(max(independent_percentage_array))]

lowest_independent_voters = independent_votes_array[independent_votes_array.index(min(independent_votes_array))]
lowest_independent_percentage = independent_percentage_array[independent_percentage_array.index(min(independent_percentage_array))]

highest_biden_voters = biden_votes_array[biden_votes_array.index(max(biden_votes_array))]
highest_biden_percentage = biden_percentage_array[biden_percentage_array.index(max(biden_percentage_array))]

lowest_biden_voters = biden_votes_array[biden_votes_array.index(min(biden_votes_array))]
lowest_biden_percentage = biden_percentage_array[biden_percentage_array.index(min(biden_percentage_array))]

highest_trump_voters = trump_votes_array[trump_votes_array.index(max(trump_votes_array))]
highest_trump_percentage = trump_percentage_array[trump_percentage_array.index(max(trump_percentage_array))]
lowest_trump_voters = trump_votes_array[trump_votes_array.index(min(trump_votes_array))]
lowest_trump_percentage = trump_percentage_array[trump_percentage_array.index(min(trump_percentage_array))]

state_greatest_margin_percentage = states_array[differential_percentage_array.index(max(differential_percentage_array))]
state_thinnest_margin_percentage = states_array[differential_percentage_array.index(min(differential_percentage_array))]
state_greatest_margin_votes = states_array[differential_votes_array.index(max(differential_votes_array))]
state_thinnest_margin_votes = states_array[differential_votes_array.index(min(differential_votes_array))]

greatest_margin_percentage = differential_percentage_array[differential_percentage_array.index(max(differential_percentage_array))]
thinnest_margin_percentage = differential_percentage_array[differential_percentage_array.index(min(differential_percentage_array))]
greatest_margin_votes = differential_votes_array[differential_votes_array.index(max(differential_votes_array))]
thinnest_margin_votes = differential_votes_array[differential_votes_array.index(min(differential_votes_array))]


print("\n\n\n")
print("*" * 120)
print("{:*^120}".format("E*L*E*C*T*I*O*N***I*N*S*I*G*H*T*S"))
print("*" * 120 + "\n")

print("{:<25s}{:<15s}{:<25s}{:<20s}".format('CATEGORY', 'CANDIDATE', 'RESULT', 'NUMBER'))
print("-" * (25 + 15 + 25 + 20))
print("{:<25s}{:<15s}{:<25s}{:<20,d}".format('Greatest Number', 'Biden', state_highest_biden_voters, highest_biden_voters))
print("{:<25s}{:<15s}{:<25s}{:<20,d}".format('Greatest Number', 'Trump', state_highest_trump_voters, highest_trump_voters))
print("{:<25s}{:<15s}{:<25s}{:<20,d}".format('Greatest Number', 'Independent', state_highest_independent_voters, highest_independent_voters))

print("\n{:<25s}{:<15s}{:<25s}{:<20,d}".format('Lowest Number', 'Biden', state_lowest_biden_voters, lowest_biden_voters))
print("{:<25s}{:<15s}{:<25s}{:<20,d}".format('Lowest Number', 'Trump', state_lowest_trump_voters, lowest_trump_voters))
print("{:<25s}{:<15s}{:<25s}{:<20,d}".format('Lowest Number', 'Independent', state_lowest_independent_voters, lowest_independent_voters))

print("\n{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Greatest Percentage', 'Biden', state_highest_biden_percentage, highest_biden_percentage))
print("{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Greatest Percentage', 'Trump', state_highest_trump_percentage, highest_trump_percentage))
print("{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Greatest Percentage', 'Independent', state_highest_independent_percentage, highest_independent_percentage))

print("\n{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Least Percentage', 'Biden', state_lowest_biden_percentage, lowest_biden_percentage))
print("{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Least Percentage', 'Trump', state_lowest_trump_percentage, lowest_trump_percentage))
print("{:<25s}{:<15s}{:<25s}{:<20.2%}".format('Least Percentage', 'Independent', state_lowest_independent_percentage, lowest_independent_percentage))
print("-" * (25 + 15 + 25 + 20))

print("\n\n{:<25s}{:<25s}{:<20s}".format('CATEGORY', 'RESULT', 'NUMBER'))
print("-" * (25 + 25 + 20))
print("{:<25s}{:<25s}{:<20.2%}".format('Greatest Margin %', state_greatest_margin_percentage, greatest_margin_percentage))
print("{:<25s}{:<25s}{:<20.2%}".format('Lowest Margin %', state_thinnest_margin_percentage, thinnest_margin_percentage))
print("\n{:<25s}{:<25s}{:<20,d}".format('Greatest Vote Margin', state_greatest_margin_votes, greatest_margin_votes))
print("{:<25s}{:<25s}{:<20,d}".format('Lowest Vote Margin', state_thinnest_margin_votes, thinnest_margin_votes))
