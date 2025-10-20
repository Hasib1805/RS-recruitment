from math import hypot

#Constructs an initial route using the nearest neighbour algorithm
def nearest_neighbour(destinations):
    start = destinations[0]
    not_visited = destinations[1:].copy() #Shallow copy
    route = [start]

    #loop until all points are added to the route
    while not_visited:
        latest = route[-1] #Current location is the most recently added point

        #Finding the closest point among not_visited destinations
        nxt_indx, nxt_coord = min(enumerate(not_visited), key = lambda item : hypot(item[1][0] - latest[0], item[1][1] - latest[1]))
        route.append(nxt_coord)
        not_visited.pop(nxt_indx)
    return route

#Tries to reduce the total length by reversing segments using the 2-opt algorithm
def two_opt(route, max_iters=200):
    n = len(route)
    
    #if there is not enough points 2-opt cannot be applied
    if n < 4:
        return route
    
    optimized = True
    iters = 0
    while optimized and iters < max_iters:
        optimized = False
        iters += 1
        for i in range(1, n-2):
            for k in range(i+1, n-1):
                A, B = route[i - 1], route[i]
                C, D = route[k], route[k + 1]
                current_path = hypot(B[0] - A[0], B[1] - A[1]) + hypot(D[0] - C[0], D[1] - C[1])
                proposed_path = hypot(C[0] - A[0], C[1] - A[1]) + hypot(D[0] - B[0], D[1] - B[1])
                
                #if proposed path length is less than the current path length then accept the changes
                if proposed_path + 1e-9 < current_path:
                    route[i : k+1] = reversed(route[i : k+1])
                    optimized = True
    return route

def sorter(destinations):
    route = two_opt(nearest_neighbour(destinations))
    start = route[0]
    targets = route[1:]
    destination_order = [start] + list(reversed(targets))
    return destination_order