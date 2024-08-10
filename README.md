```markdown
# Dartmouth Maps Project
### Author: Firdavs Babaev  
### Date: November 15, 2023

## Project Overview

The Dartmouth Maps Project is an interactive graphical tool designed to visualize and explore Dartmouth College's campus map. By utilizing a breadth-first search (BFS) algorithm, this tool helps users find the shortest path between two locations on the map, making navigation simple and intuitive.

## Features

- **Interactive Map Navigation**: Users can interact with the campus map by clicking on different locations, and the tool will calculate and display the shortest path between them.
- **Dynamic Visualization**: The map dynamically highlights paths, edges, and vertices, making it easy to understand connections between different points on campus.
- **Real-time Interaction**: Move your mouse over any location on the map to see the corresponding point highlighted, allowing for a smooth and responsive experience.

### How to Use

1. **Loading the Map**: When the program starts, it will automatically load a visual representation of Dartmouth College's campus map.

2. **Interacting with the Map**:
   - **Mouse Move**: Hover over any vertex (location) to see it highlighted on the map.
   - **Mouse Press**: Click on a location to set it as the starting point and then click another location to set it as the destination.
   - The shortest path between these two points will be highlighted in red.

3. **Resetting**: To calculate a new path, simply click on a new starting location and then a new destination. 

## Technical Details

- **Breadth-First Search (BFS)**: The project uses BFS to determine the shortest path between two locations. BFS is an efficient algorithm for this purpose because it systematically explores the shortest paths first in an unweighted graph.
- **Graphics Handling**: All visual elements are handled by the `cs1lib` library, which simplifies the process of drawing circles, lines, and handling mouse events.

Enjoy exploring Dartmouth's beautiful campus with the Dartmouth Maps Project! If you have any questions or feedback, feel free to reach out.
```
