OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):

    if operation == "conjunction":
        return x and y
    elif operation == "disjunction":
        return x or y
    elif operation == "implication":
        return not x or y
    elif operation == "exclusive":
        return x is not y
    elif operation == "equivalence":
        return x is y

