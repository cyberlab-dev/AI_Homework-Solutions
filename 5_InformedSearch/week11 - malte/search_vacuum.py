class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.SEARCHED = False

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    states_Searched = []
    best = 0
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = h1(fringe, best, states_Searched)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("Current state: ", node.STATE)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    #queue.insert(0, node)  # DFS
    queue.append(node)      # BFS
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue


'''
Remove first element from fringe
'''
def REMOVE_FIRST(queue):
    if len(queue) != 0:
        return queue.pop(0)
    return []


def h1(queue, best, states_Searched):
    bestSum = 0
    for node in queue:
        if node.STATE in states_Searched:
            continue
        if best == 0:
            best = node
        sumOfClean = node.STATE[1]+node.STATE[2]
        if sumOfClean>bestSum:
            best = node
            node.SEARCHED = True
    queue.remove(best)
    states_Searched.append(node.STATE)
    return best


'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 0, 0)
# Note: In this case, goal state is when vacuum goes back to location A and both A and B are clean
# Can also be: GOAL_STATE = ('B', 1, 1)
GOAL_STATE = ('A', 1, 1)

'''
Complete state space including loops back to current state
Note: with loops back to current state, the DFS can be stuck in an infinite loop,
so in that case BFS is used to find the path to the goal state
'''
#                  Current State - Actions:     ---LEFT---               ---SUCK---             ---RIGHT---
STATE_SPACE = {('A', 0, 0): [('A', 0, 0), ('A', 1, 0), ('B', 0, 0)],
               ('B', 0, 0): [('A', 0, 0), ('B', 0, 1), ('B', 0, 0)],
               ('A', 1, 0): [('A', 1, 0), ('A', 1, 0), ('B', 1, 0)],
               ('B', 0, 1): [('A', 0, 1), ('B', 0, 1), ('B', 0, 1)],
               ('B', 1, 0): [('A', 1, 0), ('B', 1, 1), ('B', 1, 0)],
               ('A', 0, 1): [('A', 0, 1), ('A', 1, 1), ('B', 0, 1)],
               ('A', 1, 1): [('A', 1, 1), ('A', 1, 1), ('B', 1, 1)],
               ('B', 1, 1): [('A', 1, 1), ('B', 1, 1), ('B', 1, 1)]
               }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
