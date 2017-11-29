# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:35:40 2017

@author: yuti
"""
a = [190, 33, 454, 3, 5, 12, 10, 2, 9]

# exchange 
def exch(a, i, min):
    t = a[i]
    a[i] = a[min]
    a[min] = t
    return(a)

    
exch(a, 2, 4)

# Selection Sorting
def selectionSort(a): 
    for i in range(0, len(a) - 1):
        print(i)
        min = i
        for pos in range(i+1, len(a) - 1):
            if (a[pos] < a[min]):
                min = pos
            exch(a, i, min)
    return(a)
        


# Insertion Sorting
def insertionSort(a): 
    for i in range(1, len(a) ):
        pos = i
        print(i)
        while (pos > 0) & (a[pos] < a[pos-1]) :
            exch(a, pos, pos-1)
            pos = pos - 1
    return(a)



def shellSort(a):
    N = len(a)
    h = 1
    while (h<N/3):
        h = 3*h
    while (h >= 1):
        i = h
        while (i < N):
            j = i
            while (j >= h and (a[j] < a[j-h])):
                exch(a, j, j-h)
                j = j - h
            i = i +1
        h = int(h/3)
    return(a)


import random

class Quick:
    def sort_main(self, a):
        random.shuffle(a)
        self.sort(a, 0, len(a)-1)
        # return(a)
        
    def sort(self, a, lo, hi):
        if(hi <= lo):
            return
        j = self.partition(a, lo, hi)
        self.sort(a, lo, j-1)
        self.sort(a, j+1, hi)
    
    #@staticmethod
    def partition(self, a, lo, hi):
        i = lo + 1
        j= hi
        v = a[lo]
        while(True):
            while (a[i] < v):
                if(i==hi): break
                i = i + 1
            while (v < a[j]):
                if(j==lo): break
                j = j - 1
            if(i >= j): break
            print(a)
            print(i)
            print(j)
            exch(a, i, j)
            
        print(a)
        print(lo)
        print(j)
        print(i)
        exch(a, lo, j)
        return j;
    

case_Quick = Quick()

case_Quick.partition(a, 0, len(a)-1)

case_Quick.sort_main(a)
            


def merge(a, lo, mid, hi):
    i = lo
    j = mid +1
    aux = list(range(lo, hi+1))
    for k in range(lo, hi+1):
        aux[k] = a[k]
        #print(k)
        
    for k in range(lo, hi):
        if i > mid: 
            a[k] = aux[j]
            j = j +1
        elif j > hi: 
            a[k]= aux[i]
            i = i +1
        elif aux[j] < aux[i]:
            a[k]= aux[j]
            j= j +1
        else:
            a[k]= aux[i]
            i = i +1

class Merge():
    def sort_main(self, a):
        #aux = a
        self.sort(a, 0, len(a)-1)
        
    def sort(self, a, lo, hi):
        if hi <= lo: 
            return
        
        mid = lo + (hi-lo)/2
        self.sort(a, lo, mid)
        self.sort(a, mid+1, hi)
        merge(a, lo, mid, hi)

case_Merge = Merge()

case_Merge.sort_main(a)    

class MergeBU():
    def sort(self, a):
        N = len(a)
        sz = 1
        while(sz <N):
            lo = 0
            while(lo < N-sz):
                print("sz = " + str(sz))
                print("lo = " + str(lo))
                print("lo+sz = " + str(lo+sz-1))
                print("min = " + str(min(lo+sz+sz-1, N-1)))
                merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N-1))
                lo = lo + sz+sz
            sz = sz + sz
            
case_MergeBU = MergeBU()

case_MergeBU.sort(a)  