def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # instantiate hash_table (ht)
    ht = {}
    # instantiate an insections list
    intersections = []
    # loop through the arrs in arrays
    for arrs in arrays:
        # loop through numbers (nums) in the arrs
        for nums in arrs:
            # if the nums are not in the ht
            if nums not in ht:
                # set the value as one
                ht[nums] = 1
            # else
            else:
                # add to the value
                ht[nums] += 1
    
    # instantiate max_value variable as the max(value) in ht
    max_value = max(ht.values())
    # for key, value in the ht items
    for key, value in ht.items():
        # if value == max_value
        if value == max_value:
            # append the key to the intersections list
            intersections.append(key)
    # return intersections
    return intersections



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
