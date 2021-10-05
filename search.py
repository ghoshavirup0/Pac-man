# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node:
    def __init__(self,cost,node,path,visited):
        self.cost=cost
        self.node=node
        self.path=path
        self.visited=visited

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    stack=Stack()
    path=[]
    min_cost=1000000
    visited=[]
    cur = Node(0,problem.getStartState(),"",visited)

    stack.push(cur)

    while not stack.isEmpty():

        cur=stack.pop()

        if problem.isGoalState(cur.node) and min_cost>cur.cost:
            path=cur.path.split(',')
            min_cost=cur.cost
            break
        if cur.node not in visited:
            visited.append(cur.node)
            
            successor = problem.getSuccessors(cur.node)
            for child,direction,cost in successor:
                if child not in visited:
                    
                    stack.push(Node(cur.cost+cost,child,cur.path+","+direction,visited))
                    
                

    if '' in path:
        path.remove('')
        
    return path




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    queue=Queue()
    path=[]
    visited=[]

    queue.push(Node(0,problem.getStartState(),"",visited))

    #visited.add(problem.getStartState())
    
    while not queue.isEmpty():
        cur=queue.pop()
        
        if problem.isGoalState(cur.node):
            path=cur.path.split(',')
            break

        if cur.node not in visited:
            visited.append(cur.node)
            
            successor = problem.getSuccessors(cur.node)
            for child,direction,cost in successor:
                if child not in visited:
                    queue.push(Node(cur.cost+cost,child,cur.path+','+direction,visited.copy()))
        
        
    if '' in path:
        path.remove('')

    return path
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = PriorityQueue()                   
    visited = []                                                                   
    path=[]
    tempPath=[]
    current_path=PriorityQueue()

    node= Node(0,problem.getStartState(),"",visited)
    pq.push(node,0)
    

    while not pq.isEmpty():
        cur = pq.pop()

        if problem.isGoalState(cur.node):
            path=cur.path.split(',')
            break

        if cur.node not in visited:
            visited.append(cur.node)
            successors = problem.getSuccessors(cur.node)
            for child,direction,cost in successors:
                if child not in visited:
                    tempnode=Node(cost+cur.cost,child,cur.path+','+direction,visited)
                    pq.push(tempnode,cost+cur.cost)
     

    if '' in path:
         path.remove('')
    return path
    



    
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = PriorityQueue()                   
    visited = []                                                                   
    path=[]
    tempPath=[]
    current_path=PriorityQueue()

    node= Node(0,problem.getStartState(),"",visited)
    pq.push(node,0)
    

    while not pq.isEmpty():
        cur = pq.pop()

        if problem.isGoalState(cur.node):
            path=cur.path.split(',')
            break

        if cur.node not in visited:
            visited.append(cur.node)
            successors = problem.getSuccessors(cur.node)
            for child,direction,cost in successors:
                if child not in visited:
                    tempnode=Node(cost+cur.cost,child,cur.path+','+direction,visited)
                    pq.push(tempnode,cost+cur.cost + heuristic(child,problem) )
     

    if '' in path:
         path.remove('')
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
