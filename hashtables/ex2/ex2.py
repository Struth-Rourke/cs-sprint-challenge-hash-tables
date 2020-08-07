#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # instantiate an empty lookup
    lookup = {}
    # iterate through the length
    for i in range(length):
        # set the destination equal to the lookup value of the ticket source
        lookup[tickets[i].source] = tickets[i].destination
    
    # instantiate list of specified routes via the lookup of the destination
    route = [lookup['NONE']]
    # while the route is not None
    while route[len(route) - 1] is not 'NONE':
        # append it to the lookup
        route.append(lookup[route[len(route)-1]])
    # return the route
    return route
