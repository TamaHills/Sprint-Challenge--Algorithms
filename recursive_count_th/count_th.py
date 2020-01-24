'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # get count of word - first character
    count = count_th(word[1:])

    # check if word is empty
    if len(word) == 0:
        return 0
    # check if first to characters equal 'th'
    elif word[:2] == 'th':
        #increment count by one
        count += 1
    
     
    # return count
    return count