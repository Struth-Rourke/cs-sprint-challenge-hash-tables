def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # instantiate an empty lookup
    lookup = {}

    # loop through the weights weights
    for idx, weight in enumerate(weights):
        # set the lookup value equal to the idx
        lookup[weight] = idx
        # difference of the two is the number necessary to hit the limit; it's
        # the expression value that solves the equation
        diff = limit - weight
        # if diff exists in the lookup
        if diff in lookup:
            # the diff value equal idx_2
            idx_2 = lookup[diff]
            # if idx > idx_2
            if idx > idx_2:
                # return them (idx, idx_2)
                return idx, idx_2
            # if idx < idx_2
            if idx < idx_2:
                # return them (idx_2, idx)
                return idx_2, idx
            # if idx == idx_2
            if idx == idx_2:
                # return them (idx + 1, idx_2)
                return idx + 1, idx_2
    
    return
