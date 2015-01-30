def count_inversion(sequence):
    sequence = list(sequence)                           # convert tuple to a list
    inversions, sequence = merge_sort_count(sequence)   # run it through our function to get the ordered sequence and
                                                        # the inversions
    return inversions


def merge_sort_count(sequence):
    inversions = 0                                      # start with zero inversions
    final = []                                          # make a returnable list

    if len(sequence) == 1:                              # if the list has one item
        return 0, sequence                              # return zero inversions and the item

    if len(sequence) == 2:                              # if it has two items
        if sequence[0] > sequence[1]:                   # and they are out of order
            inversions += 1                             # we have one inversion
            return inversions, [sequence[1],            # return that and the ordered pair
                                sequence[0]]
        else:
            return 0, sequence                          # else everything in order, just return

    if len(sequence) > 2:                               # if we have more than two items
        alist = sequence[0:int(len(sequence) / 2)]      # split the list in two
        blist = sequence[int(len(sequence) / 2):]       # so we devide the problem

        acount, asequence = merge_sort_count(alist)     # give the list to this function, which will run recursively
        bcount, bsequence = merge_sort_count(blist)     # dividing the list until len is 1 or 2
        inversions = acount + bcount                    # which it will return

        for k in range(0, len(sequence)):               # then it needs to combine all returned lists
            if asequence and bsequence:                 # and only run this if both lists are non-empty
                if asequence[0] > bsequence[0]:         # so if first item in list b is smaller than in list a
                    final.append(bsequence.pop(0))      # append that to the final list
                    inversions += len(asequence)        # and the number of inversions is all the remaining numbers in a

                else:
                    final.append(asequence.pop(0))      # else everything in order, just append and remove item from a
            else:
                final.extend(asequence)                 # if one of the lists is empty that means that the rest is in order
                final.extend(bsequence)                 # so extend final by both (we don't know which is empty)
                return inversions, final                # and break out of for loop to save time
    return inversions, final                            # if for loop finished, return results

