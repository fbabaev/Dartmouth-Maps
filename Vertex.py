#Author: Firdavs Babaev
#Date: 11/15/2023
#Purpose: Assignment 20

from cs1lib import *
RADIUS = 7.5
EDGE_WIDTH = 2

class Vertex:
    def __init__(self, vertex_name, x_vertex, y_vertex):
        self.vertex_name = vertex_name
        self.x_vertex = x_vertex
        self.y_vertex = y_vertex
        self.adj_list = []

    def vertex_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        set_fill_color(self.r, self.g, self.b)
        set_stroke_color(self.r, self.g, self.b)
        draw_circle(self.x_vertex, self.y_vertex, RADIUS)

    def vertex_surrounding(self, mx, my):
        return (self.x_vertex - RADIUS) <= mx <= (self.x_vertex + RADIUS) and \
            (self.y_vertex - RADIUS) <= my <= (self.y_vertex + RADIUS)

    def draw_edge (self, other_vertex, r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x_vertex, self.y_vertex, other_vertex.x_vertex, other_vertex.y_vertex)

    def draw_all_edges(self, r, g, b):
        for other_vertex in self.adj_list:
            self.draw_edge(other_vertex, r, g, b)


    def __str__(self):
        string = ""
        for vertex in self.adj_list:
            if self.adj_list.index(vertex) < len(self.adj_list)-1:
                string = string + vertex.vertex_name + ", "
            else:
                string = string + vertex.vertex_name

        return self.vertex_name + "; Location: " + str(self.x_vertex) + "," + str(self.y_vertex) + "; Adjacent vertices: " + string


