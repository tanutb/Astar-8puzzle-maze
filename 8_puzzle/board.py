
from pq import priorityQueue
from Node import Node

start = [
    [1 ,5 ,2],
    [8 ,6 ,7],
    ["x" ,4 ,3],
]
goal = [
    [1 ,2 ,3],
    [4 ,5 ,6],
    [7 ,8 ,"x"],
]

Start_Node = Node(start,goal)
pq = priorityQueue()
pq.push(Start_Node)
path = []
checked = []
count = 1000
while not pq.empty():
    n = pq.pop()

    for i in n.Gen_node(n):
        a = list(map(lambda x: x.data, pq.heap))
        b = list(map(lambda x: x.data, checked))
        if i.data not in a and i.data not in b:
            pq.push(i)

    checked.append(n)
    if len(checked) >= count :
        count += 1000
        print(count)

    if len(checked) >= 181440 :
        print("Something might wrong")
        break

    if n.data == goal :
        
        par = n

        while par != 0:

            path.append(par.data)

            par = par.parent

        break

del path[-1]
path = path[::-1]

for i in path:
    print("=============")
    for j in i :
        print(j)


import pygame 

def draw_rec(screen, pos, number, color = pygame.Color(0,255,0)):
    cell_size = 200
    pygame.draw.rect(screen,color, (pos[0]*cell_size +1, pos[1]*cell_size +1, cell_size -1, cell_size -1))
    screen.blit(font.render(str(number), True, (0,0,0)), (pos[0]*cell_size +75 , pos[1]*cell_size+40 ))
    pygame.display.flip()

width = 600
height = 600
cell_size = 25                                                  
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.init()
font = pygame.font.SysFont('Arial', 100)

for i in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), ( i*height /3, 0), (i*height /3, height))
    pygame.display.flip()

for i in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), ( 0 ,i*width /3), (width, i*width /3))
    pygame.display.flip()

for k in start :
    for i in k :
        draw_rec(screen,  (k.index(i),start.index(k)) , i , pygame.Color(255, 255, 255))

print("MOVE : ", len(path))

while True :
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    n = path.pop(0)
    for k in n :
        for i in k :
            if i == "x" :
                draw_rec(screen,  (k.index(i),n.index(k)) , i , pygame.Color(100, 100, 100))
            else : 
                draw_rec(screen,  (k.index(i),n.index(k)) , i , pygame.Color(255, 255, 255))                
        pygame.time.delay(100)    

    if n == goal :
        print("END")
        break

pygame.time.delay(5000)                                 #Delay after completion