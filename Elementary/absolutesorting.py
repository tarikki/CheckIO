def checkio(numbers_array):
    abs_array = [abs(x) for x in numbers_array]                     # calculate all the absolute values
    tuples= list(zip(numbers_array, abs_array))                     # make a list of tuples of (value, abs_value)
    sorted_list = sorted (tuples, key=lambda value: value[1])       # sort the tuples by the second (absolute) value
    nicely_sorted = [x[0] for x in sorted_list]                     # select all the abs_values from every tuple
                                                                    # and turn them into a list

    return nicely_sorted


