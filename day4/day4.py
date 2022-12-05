## Part 1
f = open('input.txt','r') # init the file
input = f.read() # read the file
input = input.split('\n')[0:-1] # transform the file
# init result variables
res = 0
res2 = 0
# main loop
for item in input:
    item = item.split(',') # split each line in two
    set_1 = set(range(int(item[0].split('-')[0]), int(item[0].split('-')[1])+1)) # then get the first part as a set
    set_2 = set(range(int(item[1].split('-')[0]), int(item[1].split('-')[1])+1)) # also the second part
    ints = set_1.intersection(set_2) # intersect
    if ints == set_1 or ints == set_2: # for first part
        res += 1
    if len(ints) > 0: # for second part
        res2 += 1
print('Answer to part 1:', res)
## Part 2
print('Answer to part 2:', res2)
