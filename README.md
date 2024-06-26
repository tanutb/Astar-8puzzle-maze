# A* Search Algorithm with Pygame Visualization
This repository contains Python implementations of the A* search algorithm applied to two different problems: maze solving and the 8 puzzle problem. Pygame is used for visualization, providing an interactive way to see the algorithm in action. Additionally, heapq is utilized for priority queue functionality.
# Maze Solving
The maze solving implementation allows the algorithm to navigate through a maze from a starting point to a goal point. The maze is represented as a grid, where certain cells are walls that cannot be traversed. Pygame is used to visualize the maze and the progress of the A* search algorithm as it explores possible paths.
## Usage
- Start simulation using
  ```
  python Sim.py
  ```
- A* search algorithm will find the shortest path from the starting position to the goal position.
- Pygame will display the maze and the progress of the algorithm, providing a visual representation of the pathfinding process.
## Issue 
Sometimes, A* may not provide the optimal path due to its heuristic function struggling with the Euclidean distance in a grid maze, which can lead the agent to choose diagonal paths that may not be optimal. However, this issue could also be related to my implementation, which may have suboptimal elements or bugs in certain parts

## Visualization  
<img src="https://github.com/tanutb/Astar-8puzzle-maze/blob/main/gif/maze.gif" width="400" height="400">

# 8 Puzzle Problem
The 8 puzzle problem involves rearranging a scrambled set of tiles numbered 1 through 8 within a 3x3 grid to reach a goal configuration. The A* search algorithm is used to find the shortest sequence of moves to reach the goal state.

## Usage
- Start simulation using
  ```
  python board.py
  ```
- Run the A* search algorithm to find the shortest sequence of moves to reach the goal state.
- Pygame will display the initial and goal configurations, as well as the progress of the algorithm as it searches for the solution.
- The start and end position can change in   ``` board.py ``` in ```line 6``` and ```line 21``` respectively 

## Testing
To ensure the correctness and performance of the implementations, various tests have been conducted. The 8 puzzle problem in some solution was found and take approximately an hour for configurations with 31 moves.
```
### "x" for blank position ###

start = [ 
  [8 ,6 ,7],
  [2 ,5 ,4],
  [3 ,"x" ,1]
 ]
 
 goal = [
    [1 ,2 ,3],
    [4 ,5 ,6],
    [7 ,8 ,"x"],
]
```
The shortest move is 31

## Visualization  
<img src="https://github.com/tanutb/Astar-8puzzle-maze/blob/main/gif/8puzzle.gif" width="400" height="400">
