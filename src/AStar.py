# Tugas Kecil 3 IF2211 Strategi Algoritma
# NIM / Nama    : 13517048 / Leonardo
#                 13517054 / Vinsen Marselino Andreas
# Nama File     : AStar.py
# Deskripsi     : Implementasi algoritma Astar

from ADT import *

#algoritma A Star
#matriks = Matriks
#Pstart, Pend = Point
def Astar(matriks, Pstart, Pend):
    if (matriks.getData(Pstart.getX(), Pstart.getY()) == 0): #dimulai dari jalan
        node_start = Node(None, Pstart)
        node_end = Node(None, Pend)

        candidate = []; visited = []
        candidate.append(node_start)
        #selagi masih ada kandidat
        while (len(candidate) > 0):
            idx = 0
            node_current = candidate[0]
            for i, n in enumerate(candidate):
                if (n.f() < node_current.f()):
                    idx = i
                    node_current = n #mengambil kandidat yang memiliki nilai f() terkecil

            candidate.pop(idx); visited.append(node_current)
            if (node_current.isEqual(node_end)):
                path = []
                current = node_current
                while current is not None:
                    path.append(current.pos)
                    current = current.pred
                return path[::-1] #dibalik

            else: #penelusuran belum selesai
                '''
                melakukan perjalanan sesuai arah jalan
                    0,1  = bergerak 1 ke atas
                    0,-1 = bergerak 1 ke bawah
                    1,0  = bergerak 1 ke kanan
                    -1,0 = bergerak 1 ke kiri 
                '''
                arah_jalan = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                successor = []
                for arah in arah_jalan:
                    temp_pos = Point(node_current.pos.getX() + arah[0],
                                    node_current.pos.getY() + arah[1])

                    if ((temp_pos.getX() < matriks.N) and
                        (temp_pos.getX() >= 0) and
                        (temp_pos.getY() < matriks.M) and
                        (temp_pos.getY() >= 0)):
                        #valid (ada di dalam maze)
                        if (matriks.getData(temp_pos.getX(), temp_pos.getY()) == 0):
                            #ada jalan
                            node_new = Node(node_current, temp_pos)
                            successor.append(node_new)

                for each in successor:
                    if (not each.ExistIn(visited)):
                        each.toN = node_current.g() + 1
                        each.fromN = Point.EuclideanDistance(each.pos, Pend)

                        if (not each.ExistIn(candidate)):
                            candidate.append(each)
    else: #Pstart tidak dimulai dari jalan yang ada
        raise TypeError
