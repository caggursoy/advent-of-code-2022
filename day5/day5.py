import csv, copy
import pandas as pd
## Part 1
f = open('input.txt','r') # init the file
# initialise some variables
line = ' '
inp_stk_list = []
stacks_list = []
orders_list = []
s_list = []
# read the crane list, just the image
while line != '':
    line = f.readline().strip('\n')
    inp_stk_list.append(line.split(' '))
info_line = inp_stk_list[-2] # get stack indices
no_cols = int(info_line[-1]) # number of stacks
inp_stk_list = inp_stk_list[0:-2] # get all stacks
line = ' ' # reset line
# read orders
while line != '': # while the end is reached
    line = f.readline().strip('\n') # get line
    orders_list.append(line.split(' ')) # strip orders
orders_list = orders_list[0:-1] # last line is not needed
# pad empties / useful for transposing the list in list comprehension
for i in range(len(inp_stk_list)): # iterate all stacks
    aux_list = [] # auxillary stack
    for j in range(no_cols): # iterate with number of cols / 1st dim
        if j < len(inp_stk_list[i]): # iterate in 2nd dim
            aux_list.append(inp_stk_list[i][j]) # append while transposing
        else:
            aux_list.append('') # or pad empty
    s_list.append(aux_list) # create another auxillary stack list
s_list = list(map(list, zip(*s_list))) # now save it while it is transposed
for stack in s_list: # remove the now unnecessary empty elements
    stacks_list.append([i for i in stack if i != ''])
### now the real thing starts
stacks_list2 = copy.deepcopy(stacks_list) # save for part 2
for order in orders_list: # move order by order
    amount = int(order[1]) # amount of items to move
    from_stack_no = int(order[3])-1 # from stack no
    to_stack_no = int(order[5])-1 # to stack no
    for _ in range(amount): # now move items one by one
        stacks_list[to_stack_no].insert(0,stacks_list[from_stack_no].pop(0))
out_str = '' # init output string
for stack in stacks_list: # get every last item
    out_str += stack[0] # and combine it
print('Answer to Part 1:',out_str.replace('[','').replace(']',''))
## Part 2
for order in orders_list: # now iterate in orders list again
    amount = int(order[1]) # get amount
    from_stack_no = int(order[3])-1 # get from stack no
    to_stack_no = int(order[5])-1 # get to stack no
    if amount == 1: # okay now if only 1 is moved, use the previous rule
        stacks_list2[to_stack_no].insert(0,stacks_list2[from_stack_no].pop(0))
    else: # if more than 2 is moved, move them as a block
        stacks_list2[to_stack_no] = stacks_list2[from_stack_no][0:amount] + stacks_list2[to_stack_no]
        for _ in range(amount): # but this time don't forget to pop them from the list
            stacks_list2[from_stack_no].pop(0)
out_str2 = '' # init output string
for stack in stacks_list2: # get all stacks
    out_str2 += stack[0] # combine them
print('Answer to Part 2:',out_str2.replace('[','').replace(']',''))
