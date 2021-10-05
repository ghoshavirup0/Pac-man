# Pac-man
<h2> In this project I am going to illustrate the following using our beloved Pac-man game :
  <br/>
  <ol>
    <li><a href="#search algorithms">Search algorithms (DFS, BFS, UCS, A*)</a></li>
  </ol>
</h2>

<div>
  <h2> Instructions </h2>

  Clone or download the entire package and follow instructions to run the program in your system. Make sure you have installed <a href="https://www.python.org">Python 3.7 or higher </a>.
To play the game just run the following command in command line:
   ```diff
  python pacman.py
  ```
</div>
<div>
<a name="search algorithms"></a>
<h2>Visualizaton of Search algorithms (<a href="https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/">DFS</a>, <a href="https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/">BFS</a>, <a href="https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/">UCS</a>, <a href="https://www.geeksforgeeks.org/a-search-algorithm/">A*</a>):</h2>
  

https://user-images.githubusercontent.com/57269014/135972004-908931d7-2731-4f29-a463-59413f952cc0.mp4

Pacman lives in a shiny blue world of twisting corridors and tasty round treats. Navigating this world efficiently will be Pacman's first step in mastering his domain.  
Here Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently using following algorithms:
  1. Depth First Search
  2. Breadth First Search
  3. Uniformed Cost Search
  4. A* Search

The codes are present in the following python files:
  1. ```search.py``` : Where all of the search algorithms reside.
  2. ```searchAgents.py``` : Where all of the search-based agents reside.
  
The simplest agent in ```searchAgents.py``` is called the ```GoWestAgent```, which always goes West (a trivial reflex agent). This agent can occasionally win:
  ```diff
  python pacman.py --layout testMaze --pacman GoWestAgent
  ```
But, things get ugly for this agent when turning is required:
  ```diff
  python pacman.py --layout tinyMaze --pacman GoWestAgent
  ```
The missions is to solve the problem not only for tinyMaze but for all the mazes:
  1. ```tinyMaze```
  2. ```mediumMaze```
  3. ```bigMaze```
  
  Use the following command to excecute the algorithms (DFS, BFS, UCS, A*) to solve the path finding problem for any kind of maze mentioned above.
  Just edit the <b>maze name</b> and <b>fn</b> value (i.e. <b>dfs</b>, <b>bfs</b>, <b>ucs</b>, <b>astar</b>).
  <br/>  <i>Note: <b>Heuristic</b> is only used in case of A* algorithm</i>  <br/>
  ```python pacman.py -l <maze name> -p SearchAgent -a fn=<dfs or bfs or ucs or astar> ,heuristic=manhattanHeuristic```
    <br/>
      <br/>
<b><i>Example:</b></i>  mediumMaze and bfs algorithm:
   ```diff
  python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs ,heuristic=manhattanHeuristic
  ```

  Use the following command for more complex problem (requires more computation) :
  ```diff
  python pacman.py -l testSearch -p SearchAgent -a fn=astar, prob=FoodSearchProblem, heuristic=foodHeuristic
  ```
</div>
