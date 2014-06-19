# -*- coding: cp1252 -*-
from numpy import *

def matriz_1():
    a = zeros((9,9))
    a[0] = [0,1,inf,inf,inf,inf,4,inf,10]
    a[1] = [1,0,9,inf,8,inf,inf,inf,inf]
    a[2] = [inf,9,0,2,inf,inf,inf,inf,inf]
    a[3] = [inf,inf,2,0,9,4,inf,inf,2]
    a[4] = [inf,8,inf,9,0,2,inf,inf,1]
    a[5] = [inf,inf,inf,4,2,0,inf,6,inf]
    a[6] = [4,inf,inf,inf,inf,inf,0,7,inf]
    a[7] = [inf,inf,inf,inf,inf,6,7,0,3]
    a[8] = [10,inf,inf,2,1,inf,inf,3,0]
    return a

def imprimir(a):
    bla = ['A','B','C','D','E','F','G','H','I']
    print "     A    B    C    D    E    F    G    H    I"
    for i in range(9):
        print bla[i], a[i]

def rutas(a,marcas):
    anterior = copy(a)
    contador = 0
    while True:
        contador += 1
        for i in range(9):
            for j in range(9):
                for z in range(9):
                    temp = copy(a[i,j])
                    a[i,j] = min(a[i,j], (anterior[i,z]+anterior[z,j]))
                    if (z == 7 and (i==8 or j==8)) or (z==8 and (i==7 or j==7)) or marcas[i,z]== 1 or marcas[z,j] ==1:
                        if temp != a[i,j]:
                            marcas[i,j] = 1
        if array_equal(a,anterior):
            print "Rutas minimizadas"
            break
        print "\nIteracion #",contador,":\n"
        imprimir(a)
        anterior = copy(a)
    return a

        
def main():
    a = matriz_1()
    marcas = zeros((9,9))
    print "Matriz original: \n"
    imprimir(a)
    rutas(a,marcas)
    print"\n######UN BARCO CORTA LAS LINEAS ENRE H e I #####"
    a[7,8] = float("inf")
    a[8,7] = float("inf")
    for m in range(9):
        for n in  range(9):
            if marcas[m,n] == 1:
                a[m,n]=float("inf")
    print "Se deconocen los costos que pasaban por esa linea:\n"
    imprimir(a)
    rutas(a, marcas)
    

if __name__ == '__main__':
    main()
