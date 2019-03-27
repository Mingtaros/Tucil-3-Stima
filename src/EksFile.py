# Tugas Kecil 3 IF2211 Strategi Algoritma
# NIM / Nama    : 13517048 / Leonardo
#                 13517054 / Vinsen Marselino Andreas
# Nama File     : EksFile.py
# Deskripsi     : Pembacaan file
from ADT import *

def AmbilData(file_name):
    list_input = []
    n_kolom = 0
    n_baris = 1
    check_baris = True

    mat_file = open(file_name,'r')
    a = mat_file.read(1)
    while (a!=""):
        if(a == '1' or a == '0'):
            list_input.append(a)
            if(check_baris):
                n_kolom += 1
        elif(a == '\n'):
            n_baris += 1
            check_baris = False
        a = mat_file.read(1) #baca 1 karakter

    iter_baris = 0
    iter_kolom = 0
    matriks_maze = Matriks(n_baris,n_kolom)
    for i in list_input:
        matriks_maze.AddData(iter_baris,iter_kolom,i)
        iter_kolom += 1
        if(iter_kolom == n_kolom):
            iter_baris += 1
            iter_kolom = iter_kolom % n_kolom

    return matriks_maze