import csv
## Part 1
with open('input.txt', 'r') as f_input:
    csv_input = csv.reader(f_input, delimiter=' ', skipinitialspace=True)
    opp = []
    me = []
    for cols in csv_input:
        opp.append(cols[0])
        me.append(cols[1])

print(opp)
print(me)
score = 0
for i in range(len(opp)):
    game_str = opp[i]+me[i]
    if game_str == 'BX':
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
        score += 3+3
    elif game_str == 'BY':
        # draw
        score += 2+3
    elif game_str == 'CZ':
        # draw
        score += 1+3
    else:
        score += 6
        if me[i] == 'X':
            score += 3
        elif me[i] == 'Y':
            score += 2
        elif me[i] == 'Z':
            score += 1
        # me win
print(score)
    # if me[i] == 'X':
    #     if opp[i] == 'B':
    #         # opp win
    #     else:
    #
    # elif me[i] == 'Y':
    #     if opp[i] == 'C':
    #         # opp win
    #     else:
    #
    # elif me[i] == 'Z':
    #     if opp[i] == 'A':
    #         # opp win
    #     else:
