# Tugas Kecil 3 IF2211 Strategi Algoritma
# NIM / Nama    : 13517048 / Leonardo
#                 13517054 / Vinsen Marselino Andreas
# Nama File     : ADT.py
# Deskripsi     : Tipe bentukan untuk Point, Matriks

from colorama import Back, Style
import numpy as np
from math import sqrt

class Point:
    def __init__(self, _x = 0, _y = 0):
        self.x = _x
        self.y = _y

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    @staticmethod
    def EuclideanDistance(P1, P2): #P1 dan P2 = Point
        return sqrt((P1.x - P2.x)**2 + (P1.y - P2.y)**2)

#matriks NxM
class Matriks:
    def __init__(self, _n = 0, _m = 0):
        self.N = _n
        self.M = _m
        self.data = np.zeros((self.N, self.M), dtype = int)

    def AddData(self, i, j, value):
        self.data[i][j] = value

    def getData(self, i, j):
        return self.data[i][j]

    def Print(self):
        for i in range(self.N):
            for j in range(self.M):
                if (self.getData(i,j) == 1):
                    print(Back.LIGHTBLACK_EX + " ", end = " ")
                    print(Style.RESET_ALL, end = "")
                elif (self.getData(i,j) == 2):
                    print(Back.GREEN + " ", end = " ")
                    print(Style.RESET_ALL, end = "")
                else: #self.getData(i,j) == 0
                    print(Back.WHITE + " ", end = " ")
                    print(Style.RESET_ALL, end = "")
            print(Style.RESET_ALL)

class Node:
    def __init__(self, _pred = None, _position = Point()):
        self.pred = _pred
        self.position = _position

        self.toN = 0
        self.fromN = 0

    def isEqual(self, node2):
        return ((self.position.x == node2.position.x) and
                (self.position.y == node2.position.y))

    def ExistIn(self, listOfNode):
        for v in listOfNode:
            if (self.isEqual(v)):
                return True
            else:
                continue
        #sampai bagian ini jika self tidak exist di listOfNode
        return False

    def search(self, listOfNode):
        for v in listOfNode:
            if (self.isEqual(v)):
                return v.pred
            else:
                continue
        #sampai bagian ini jika self tidak exist di listOfNode
        return False

    def g(self):
        return self.toN
    
    def h(self):
        return self.fromN

    def f(self):
        return self.g() + self.h()