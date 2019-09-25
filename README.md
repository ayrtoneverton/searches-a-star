# A* Search Algorithm Implementations
These are two algorithmic implementations of A*(A Star) in Python, where one uses a matrix for navigation and another uses a graphs structure, but not completely, because it uses part of python's own structure, for example it was created the Vertex class and for the edges were used a map with the item names to a list of tuples containing the target item names and the weight of that edge. That way, from each vertex, we can know the path and weight to their adjacent.

## Prerequisites
It takes Python 3 to execute the ".py" files and Jupyter Notebook (IPython) to execute the ".ipynb" files.

## Code Structure

* In a-star-matrix:
  - a_star_char(maze_char):
    - This function receives a character array where "A" represents the beginning and "B" the end of the path, "0" (zero character) represents the map navigable path, and "1" (character one) represents the non-navigable path. The function extracts the beginning and end of the search and converts the array to an array with integers previously represented as characters, and finally returns the a_star call.
  - a_star(maze, start, end):
    - This function receives an array of integers (the map), a start and end search position, in the matrix the "0" (number zero) represents the navigable path through the map and the "1" (number one) represents the non-navigable path. The function uses the A* algorithm to identify the best path and return it.
* In a-star-graphs:
  - a_star_list(vertices_list, edges_list, start_char, end_char)
    - This function receives a list of vertices as tuples in the format "(position X, position Y,  name char)", it also receives a list of edges as tuples in the format "(char origin, char destine, cost)", the name char of the beginning and the char name of the end. The function converts the vertex list into Vertex object map for easy access and edges to a map where the vertex char name is the key and the adjacent vertex list is the content, and converts the beginning and end to their elements. All this to pass everything treated to a_star.
  - a_star(vertices_map, edges_map, start, end)
    - The function uses the A* algorithm to identify the lowest cost path and return a sequence of vertex char names and your cost.
