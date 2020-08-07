def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # instantiate a lookup using list comp
    lookup = {i: -i for i in a if i < 0}
    # set a result list to hold all the values that have a negative
    result = []
    # loop through the lookup
    for n in lookup:
        # is the value is in a
        if lookup[n] in a:
            # append it to result
            result.append(lookup[n])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
