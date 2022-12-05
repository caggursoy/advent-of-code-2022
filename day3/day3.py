## Part 1
f = open('input.txt','r') # init the file
input = f.read() # read the file
input = input.split('\n')[0:-1] # transform the file
sum_prior = 0
for inp_str in input:
    str_1 = inp_str[0:int(len(inp_str)/2)] # get the first str
    str_2 = inp_str[int(len(inp_str)/2):int(len(inp_str))] # now the second str
    common_char = list(set(str_1).intersection(set(str_2)))[0] # and intersect them in set logic
    if common_char.isupper(): # use ASCII logic now
        sum_prior += ord(common_char)-38 # but -38 as per the provided rule
    elif common_char.islower():
        sum_prior += ord(common_char)-96 # again -96 as per the provided rule
print('Answer to part 1:', sum_prior)
## Part 2
# read 3 line by 3 line
sum_prior2 = 0
for i in range(0,len(input),3):
    str_1 = input[i] # now get the required
    str_2 = input[i+1] # lines one
    str_3 = input[i+2] # by one
    common_char = list(set(str_1).intersection(set(str_2).intersection(set(str_3))))[0] # again get the common element with set logic
    if common_char.isupper(): # use ASCII logic
        sum_prior2 += ord(common_char)-38
    elif common_char.islower(): # to get the result
        sum_prior2 += ord(common_char)-96
print('Answer to part 1:', sum_prior2)
