"""
A* Search#
Both Greedy Breadth-First Search and A* use a heuristic function. 
The only difference is that A* uses both the heuristic and the ordering from Dijkstra’s Algorithm. 

"""

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]



def heuristic(a,b):
    (x1,y1) = a
    (x2,y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    """
    Implementing A * search
    """
    frontier  = PriorityQueue()
    frontier.put(start,0)
    came_from = {}
    cost_so_far = {}

    came_from[start]  = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current  = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next]  =  new_cost
                priority =  new_cost + heuristic(goal,next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

# Trying the code here..
from implementation import *

start,goal =  (1,4),(7,8)

came_from, cost_so_far = a_star_search(diagram4, start,goal)
draw_grid(diagram4,width=3, point_to = came_from, start = start, goal=goal)
print()

draw_grid(diagram4,width=3, number = cost_so_far, start=start, goal=goal)