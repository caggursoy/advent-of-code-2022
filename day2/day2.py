import csv
## Part 1
with open('input.txt', 'r') as f_input: # read the file
    csv_input = csv.reader(f_input, delimiter=' ', skipinitialspace=True) # csv.reader is better for multi-columns
    opp = []
    me = []
    for cols in csv_input: # now get the cols into seperate lists
        opp.append(cols[0])
        me.append(cols[1])
score = 0 # init score ofc
for i in range(len(opp)): # now loop over the most boring solution ever lol
    game_str = opp[i]+me[i] # create a combined game string
    if game_str == 'BX': # and basically if-else through all possible scenarios
        # opp win
        score += 1
    elif game_str == 'CY':
        # opp win
        score += 2
    elif game_str == 'AZ':
        # opp win
        score += 3
    elif game_str == 'AX':
        # draw
        score += 1+3
    elif game_str == 'BY':
        # draw
        score += 2+3
    elif game_str == 'CZ':
        # draw
        score += 3+3
    else:
        # me win
        score += 6
        if me[i] == 'X':
            score += 1
        elif me[i] == 'Y':
            score += 2
        elif me[i] == 'Z':
            score += 3
print('Answer to part 1 is:', score)

## Part 2
score_2 = 0
for j in range(len(opp)): # do the same thing for the second part, but with new rules
    round_result = me[j]
    opp_cho = opp[j]
    if round_result == 'X': # lose
        if opp_cho == 'A':
            score_2 += 3
        elif opp_cho == 'B':
            score_2 += 1
        elif opp_cho == 'C':
            score_2 += 2
    elif round_result == 'Y': # draw
        score_2 += 3
        if opp_cho == 'A':
            score_2 += 1
        elif opp_cho == 'B':
            score_2 += 2
        elif opp_cho == 'C':
            score_2 += 3
    elif round_result == 'Z': # win
        score_2 += 6
        if opp_cho == 'A':
            score_2 += 2
        elif opp_cho == 'B':
            score_2 += 3
        elif opp_cho == 'C':
            score_2 += 1

print('Answer to part 2 is:', score_2)
