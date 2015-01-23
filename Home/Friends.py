def check_connection(network, first, second):
    # Build the network
    friendSets = []

    for member in network:                  # Go through all the pairs in the network
        presentIn = []
        member = set(member.split('-'))     # Split them and turn them into a set
        for i in range(0, len(friendSets)): # Iterate through all sets of friends
            if friendSets[i] & member:      # If the intersection yields a positive result,
                presentIn.append(i)         # make a note to which set members belong to
        for i in range(0, len(presentIn)):  # append the members to all sets even one of them is part of
            friendSets[presentIn[i]] = friendSets[presentIn[i]] | member
        if len(presentIn) == 0:             # if they are not present in any sets, make a new one
            friendSets.append(member)       # this will also take care of the start where there are no sets

    noChanges = False
    while not noChanges:                    # this loop merges all sets with common members
        noChanges = True                    # we always assume we're done
        a = len(friendSets)
        if a > 1:                           # if there is only one set, no merging required
            for i in range(1, a):           # loop through all sets
                    if i < a:               # safety for not checking out of bounds members
                        if friendSets[i] & friendSets[i-1]:     # if the intersection of two consecutive sets is not none
                            friendSets[i] = friendSets[i] | friendSets[i-1]     #merge them
                            del friendSets[i-1]                 # and delete the redundant one
                            a = a -1                            # adapt the length of the loop to our new set size
                            noChanges = False                   # and signal to the while loop that we made changes

    bros = {first, second}                  # turn the members to check into a set
    connected = False
    for friendSet in friendSets:
        if friendSet & bros == bros:        # if the intersection is the same as the bros set
            connected = True                # they are connected because they are part of the same set

    return connected
