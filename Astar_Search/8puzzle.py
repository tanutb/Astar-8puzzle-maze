import copy
from turtle import pu
puzzle = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , "x"]]

Start = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , "x" , 8]]


# import pygame 

# def draw_rec(screen, pos, number, color = pygame.Color(0,255,0)):
#     cell_size = 200
#     pygame.draw.rect(screen,color, (pos[0]*cell_size +1, pos[1]*cell_size +1, cell_size -1, cell_size -1))
#     screen.blit(font.render(str(number), True, (0,0,0)), (pos[0]*cell_size +75 , pos[1]*cell_size+40 ))
#     pygame.display.flip()

# width = 600
# height = 600
# cell_size = 25                                                  
# screen = pygame.display.set_mode((width, height))
# screen.fill((255, 255, 255))
# pygame.init()
# font = pygame.font.SysFont('Arial', 100)

# for i in range(1, 3):
#     pygame.draw.line(screen, (0, 0, 0), ( i*height /3, 0), (i*height /3, height))
#     pygame.display.flip()

# for i in range(1, 3):
#     pygame.draw.line(screen, (0, 0, 0), ( 0 ,i*width /3), (width, i*width /3))
#     pygame.display.flip()

# for k in puzzle :
#     for i in k :
#         draw_rec(screen,  (k.index(i),puzzle.index(k)) , i , pygame.Color(255, 255, 255))




class Node:
    def __init__(self,parent,data):
        self.parent = parent
        self.gen = 0
        self.data = data
        self.stat = ""
        self.fval = 0
        self.cost = 0
    

    def up(self,index_xr,index_xc):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr+1][index_xc]
        c_data[index_xr+1][index_xc] = "x"
        a = Node(self.parent,c_data)
        a.stat = "UP"
        a.gen = self.gen + 1
        a.cost = a.h()
        return a

    def right(self,index_xr,index_xc):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr][index_xc-1]
        c_data[index_xr][index_xc-1] = "x"
        a = Node(self.parent,c_data)
        a.stat = "right"
        a.gen = self.gen + 1
        a.cost = a.h()
        return a

    def down(self,index_xr,index_xc):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr-1][index_xc]
        c_data[index_xr-1][index_xc] = "x"
        a = Node(self.parent,c_data)
        a.stat = "down"
        a.gen = self.gen + 1
        a.cost = a.h()
        return a

    def left(self,index_xr,index_xc):
        w_data = copy.deepcopy(self.data)
        w_data[index_xr][index_xc] = w_data[index_xr][index_xc+1]
        w_data[index_xr][index_xc+1] = "x"
        e = Node(self.parent,w_data)
        e.stat = "left"
        e.gen = self.gen + 1
        e.cost = e.h()
        return e

    def get_parent(self):
        return str(str(self.parent) + self.stat)

    def nei(self):   
        if self.data[0][0] == 'x':
            return [self.up(0,0),self.left(0,0)]
        elif self.data[0][1] == 'x':
            return [self.up(0,1),self.left(0,1),self.right(0,1)]
        elif self.data[0][2] == 'x':
            return [self.up(0,2),self.right(0,2)]
        elif self.data[1][0] == 'x':
            return [self.up(1,0),self.right(1,0),self.down(1,0)]
        elif self.data[1][1] == 'x':
            return [self.up(1,1),self.right(1,1),self.down(1,1),self.left(1,1)]
        elif self.data[1][2] == 'x':
            return [self.up(1,2),self.right(1,2),self.down(1,2)]
        elif self.data[2][0] == 'x':
            return [self.down(2,0),self.left(2,0)]
        elif self.data[2][1] == 'x':
            return [self.down(2,1),self.left(2,1),self.right(2,1)]
        elif self.data[2][2] == 'x':
            return [self.down(2,2),self.right(2,2)]
        return None

    def h(self):
        h = 0
        for i in range(len(self.data)) :
            for j in range(len(self.data)) :
                if self.data[i][j] != puzzle[i][j] and self.data[i][j] != 'x':
                    h+=1
        return h

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def h(data,puzzle):
    h = 0
    for i in range(len(data)) :
        for j in range(len(data)) :
            if data[i][j] != puzzle[i][j] and data[i][j] != 'x':
                h+=1
    return h

from heapq import heappush, heappop
class priorityQueue:

    # Constructor to initialize a
    # Priority Queue
    def __init__(self):
        self.heap = []
 
    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)
 
    # Method to remove minimum element
    # from Priority Queue
    def pop(self):
        return heappop(self.heap)
 
    # Method to know if the Queue is empty
    def empty(self):
        if not self.heap:
            return True
        else:
            return False

a = [ [ 1, 2, 3 ],
     [ 5, 6, "x" ],
    [ 7, 8, 4 ] ]

puzzle = [ [ 1, 2, 3 ],
          [ 5, 8, 6 ],
          [ "x", 7, 4 ] ]
    
print(h(a,puzzle))

Start_node = Node(0,a)
# for i in Start_node.nei():
#     print(i.data)
pq = priorityQueue()
pq.push(Start_node)

while not pq.empty() :
    n = pq.pop()
    print(n.stat)
    for i in n.data :
        print(i)
    print("===========")

    if n.data == puzzle:
        break
    
    for i in n.nei():
        pq.push(i)

    # A = copy.deepcopy(pq)
    # print(A.heap)

    
