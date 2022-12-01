## Part 1
f = open('input.txt','r') # init the file
input = f.read() # read the file
input = input.split('\n') # transform the file
sum = 0 # init sum
sum_list = [] # init sum list
for el in input: # ye good olde for looping
    if el == '': # obviously check for this fella
        sum_list.append(sum) # save the sum
        sum = 0 # reset the sum
    else:
        sum += int(el) # sum the calorie of the elf
aux_list = sum_list[:] # important for part 2
sum_list.sort() # sorttt the elvesss
print('Answer to part1:', sum_list[-1])
## Part 2
sum_top = 0 # init the top 3 sum
for _ in range(3): # we only need top 3
    top_sum_elf = sum_list.pop() # poppp the top calorie elf
    top_elf_ind = aux_list.index(top_sum_elf) # find the index / have no idea why but still
    sum_top += top_sum_elf # sum the top elves' calories
print('Answer to part2:', sum_top)
