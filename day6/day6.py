from collections import Counter
## Part 1 & 2
f = open('input.txt','r') # init the file
inp_str = f.readlines()[0].strip('\n')
buff_len = [4,14] # 4 for part 1, 14 for part 2
# define a uniqueness function
def unq_chars(input):
    # get frequency
    freq = Counter(input)
    if(len(freq) == len(input)): # compare with the input
        return True
    else: # if the size is the same, the str is unique
        return False
for bu_len in buff_len: # loop over for both parts
    for ind in range(0,len(inp_str)-bu_len): # get the slicing index
        buffer = inp_str[ind:ind+bu_len] # slice the input and get the buffer
        if unq_chars(buffer): # if all chars are unique in the buffer
            print('Answer to part', buff_len.index(bu_len)+1, 'is:', ind+bu_len) # stop the code and print the answer
            break
