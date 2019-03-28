# Tugas Kecil 3 IF2211 Strategi Algoritma
# NIM / Nama    : 13517048 / Leonardo
#                 13517054 / Vinsen Marselino Andreas
# Nama File     : BFS.py
# Deskripsi     : Implementasi algoritma BFS
from ADT import *

def BFS(maze, start, end):
    if(maze.data[start.x][start.y] == 0 and maze.data[end.x][end.y] == 0):
        visited = []
        queue = []
        curr_node = Node(None, start)

        queue.append(curr_node)
        while (queue != [] and curr_node.pos != end): 
            curr_node = queue.pop(0)
            prev_node = curr_node
            if(not(curr_node.ExistIn(visited))):
                visited.append(curr_node)
                if(curr_node.pos.x+1 < maze.N):
                    if (maze.data[curr_node.pos.x+1][curr_node.pos.y] == 0):
                        next_pos = Point(curr_node.pos.x+1,curr_node.pos.y)
                        next_node = Node(prev_node, next_pos)
                        queue.append(next_node)
                if(curr_node.pos.x-1 >= 0):
                    if (maze.data[curr_node.pos.x-1][curr_node.pos.y] == 0):
                        next_pos = Point(curr_node.pos.x-1,curr_node.pos.y)
                        next_node = Node(prev_node, next_pos)
                        queue.append(next_node)
                if(curr_node.pos.y+1 < maze.M):
                    if (maze.data[curr_node.pos.x][curr_node.pos.y+1] == 0):
                        next_pos = Point(curr_node.pos.x,curr_node.pos.y+1)
                        next_node = Node(prev_node, next_pos)
                        queue.append(next_node)
                if(curr_node.pos.y-1 >= 0):
                    if (maze.data[curr_node.pos.x][curr_node.pos.y-1] == 0):
                        next_pos = Point(curr_node.pos.x,curr_node.pos.y-1)
                        next_node = Node(prev_node, next_pos)
                        queue.append(next_node)
        if (curr_node.pos == end):
            path = [end]
            start_node = Node(None,end)
            while(start_node.pos != start):
                path_node = start_node.search(visited)
                path.append(path_node.pos)
                start_node = path_node
            path.append(start)
            return path[::-1]
