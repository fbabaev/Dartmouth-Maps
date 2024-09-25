#Author: Firdavs Babaev
#Date: 11/15/2023
#Purpose: Dartmouth Maps Project

from Vertex import Vertex

def load_grap(file_name):


#first pass: creates the vertex objects and dictionary entries
    file = open(file_name, "r")
    vertex_dictionary = {}

    for line in file:
        data = line.strip().split(";")

        #Extract vertex name, adjacent vertices, and coordinates
        vertex_name = data[0].strip()
        coordinates = data[2].strip().split(",")
        vertex = Vertex(vertex_name, int(coordinates[0]), int(coordinates[1]))  # add vertex name and coordinates
        vertex_dictionary[data[0]] = vertex

    file.close()

#Second pass: Populates adjacency lists
    file = open(file_name, "r")

    for line in file:
        data = line.strip().split(';')
        vertex_name = data[0].strip()
        adjacent_vertices = data[1].strip().split(',')

        for adjacent_vertex_name in adjacent_vertices:
            vertex_dictionary[vertex_name].adj_list.append(vertex_dictionary[adjacent_vertex_name.strip()])

    file.close()
    return vertex_dictionary
