# Tugas Kecil 3 IF2211 Strategi Algoritma
# NIM / Nama    : 13517048 / Leonardo
#                 13517054 / Vinsen Marselino Andreas
# Nama File     : MainProg.py
# Deskripsi     : Memanggil algoritma A* dan BFS untuk mendapatkan path pada maze

from colorama import init
from AStar import *
from BFS import *
from EksFile import *

if __name__ == '__main__':
    init() #colorama
    try:
        file_name = str(input("Masukkan nama file yang berisi matriks(.txt): "))
        matAStar = AmbilData(file_name)
        matBFS = AmbilData(file_name)
        print("Maze =")
        matAStar.Print()
        x0 = input("Masukkan x1 dan y1 (dipisah spasi) = ")
        x1, y1= int(x0.split()[0]), int(x0.split()[1])
        x0 = input("Masukkan x2 dan y2 (dipisah spasi) = ")
        x2, y2 = int(x0.split()[0]), int(x0.split()[1])
        start_point = Point(x1, y1)
        end_point = Point(x2, y2)
        print("\nHasil Algoritma A* =")
        try:
            path = Astar(matAStar, start_point, end_point)
            for ea in path:
                matAStar.AddData(ea.getX(), ea.getY(), 2)
            matAStar.Print()
        except (TypeError):
            print("Path tidak ditemukan!")

        print("\nHasil Algoritma BFS =")
        try:
            path = BFS(matBFS, start_point, end_point)
            for ea in path:
                matBFS.AddData(ea.getX(), ea.getY(), 2)
            matBFS.Print()
        except (TypeError):
            print("Path tidak ditemukan!")
    except (FileNotFoundError):
        print("File tidak ditemukan")
    
