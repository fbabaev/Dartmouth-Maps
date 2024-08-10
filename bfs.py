#Author: Firdavs Babaev
#Date: 11/15/2023
#Purpose: Dartmouth Maps Project

from collections import deque
def breadth_first(start, goal):
    backpointer = {}
    queue = deque()
    queue.append(start)
    backpointer[start] = None

    while len(queue) != 0:
        current_vertex = queue.popleft() #Go to the next vertex from the front of queue

        if current_vertex == goal:
            vertex_path = [] #List to stores the vertices in the shortest path
            vertex_path.append(current_vertex) #Add current vertex to the path

            while backpointer[current_vertex] is not None:
                #Traverse the backpointer dictionary to construct the shortest path from goal to the start vertex
                vertex_path.append(backpointer[current_vertex])
                current_vertex = backpointer[current_vertex]

        for neighbor in current_vertex.adj_list:
            if neighbor not in backpointer:
                #If the neighboring vertex has not been visited, add it to the backpointer and the queue
                backpointer[neighbor] = current_vertex
                queue.append(neighbor)

    return vertex_path #RETURN THE SHORTEST PATH FROM THE INITIAL TO THE GOAL
