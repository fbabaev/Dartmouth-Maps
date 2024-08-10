#Author: Firdavs Babaev
#Date: 11/15/2023
#Purpose: Assignment 20

from Vertex import *
from load_graph import *
from bfs import *

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
vertex_initial = None
vertex_final = None
bx = None
by = None
ax = None
ay = None
mouse_pressed = False
mouse_move = False
my_vertex_path = []

#Load the graph from the file
vertex_dictionary = load_graph("dartmouth_graph")

def my_mouse_move(mx, my):
    global mouse_move, bx, by, vertex_final
    #Check if mouse is on a vertex
    for vertex in vertex_dictionary:
        if vertex_dictionary[vertex].vertex_surrounding(mx, my):
            mouse_move = True
            bx = vertex_dictionary[vertex].x_vertex
            by = vertex_dictionary[vertex].y_vertex
            vertex_final = vertex_dictionary[vertex]

def my_mouse_press(mx,my):
    global mouse_pressed, ax, ay, vertex_initial
   #Check if mouseis pressed on a vertex
    for vertex in vertex_dictionary:
        if vertex_dictionary[vertex].vertex_surrounding(mx, my):
            mouse_pressed = True
            ax = vertex_dictionary[vertex].x_vertex
            ay = vertex_dictionary[vertex].y_vertex
            vertex_initial = vertex_dictionary[vertex]

img = load_image("dartmouth_map.png")
def my_draw():
    global vertex_initial, vertex_final, mouse_pressed\
        , mouse_move, ax, ay, bx, by, img, vertex_dictioary\
        , my_vertex_path


    draw_image(img, 0, 0)

    for vertex in vertex_dictionary:
        vertex_dictionary[vertex].vertex_color(0, 0, 1)
        vertex_dictionary[vertex].draw_all_edges(0, 0, 1)


    if mouse_pressed:
        set_fill_color(1, 0, 0)
        set_stroke_color(1, 0, 0)
        draw_circle(ax, ay, RADIUS)

        if mouse_move:
            set_fill_color(1, 0, 0)
            set_stroke_color(1, 0, 0)
            draw_circle(bx, by, RADIUS)

            if vertex_initial != vertex_final:
               #Find the shorted path using the breadth-first search
                my_vertex_path = breadth_first(vertex_initial, vertex_final)


                #Draw the path and the color
                for i in range(len(my_vertex_path)):
                    if i != len(my_vertex_path)-1:
                        my_vertex_path[i].vertex_color(1, 0, 0)
                        my_vertex_path[i].draw_edge(my_vertex_path[i+1], 1, 0, 0)


start_graphics(my_draw, 2400,  width = WINDOW_WIDTH, height = WINDOW_HEIGHT, mouse_press = my_mouse_press, mouse_move = my_mouse_move)