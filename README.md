# Details
Algorithm that used in code is A* search

## A* search with maze 
- If you need the performance not the shortest path, just remove seld.d (level of node) update
**but it can make it error and bug**
- Just update level to cost to make it shortest path and prevent bugs
**but it will take a time longer**
## 8 puzzle 
- It can find the shortest move within a few seconds if it's around 20 moves only
more than that, it will take a long time 

for test 
```
"x" for blank positon

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
