# Details
Algorithm that used in code is A* search

## A* search with maze 
-if you need the peformance not shortest path just remove seld.d (level of node) update 
but it can make the it error and bug
-Just update level to cost to make it shortest path and prevent bugs

## 8 puzzle 
- it can find the shortest move within a few second if it's around 20 move only
more than that it will take a long time 

for test 
```
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

the shortest move is 31
>But it thake an hour to find that
