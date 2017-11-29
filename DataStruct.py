# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:14:31 2017

@author: yuti
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
        
n1 = Node(123)



class Queue():
    def __init__(self):
        self.first = None
        self.last = self.first
        self.N = 0
    
    def isEmpty(self):
        return(self.first == None)
    
    def size(self):
        return self.N
    
    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item)
        self.last.next = None
        
        if(self.isEmpty()):
            self.first = self.last
        else: 
            oldlast.next = self.last
        self.N = self.N + 1
        
    def dequeue(self):
        item = self.first.getData()
        self.first = self.first.getNext()
        if (self.isEmpty()):
            self.last = None
        self.N = self.N - 1
        return(item)
        
class SequentialSearchST():
    
    class Node:
        def __init__(self,value, key, nextnode = None):
            self.value = value
            self.key = key
            self.next = nextnode
    
    def __init__(self):
        self.first = None
    
    def get(self, key):
        x = self.first
        while x != None:
            if(key == x.key):
                return(x.value)
            x = x.next
        return None
    
    def put(self, key, val):
        x = self.first
        while x != None:
            if(key == x.key):
                x.value = val
                return
            x = x.next
        self.first = self.Node(val, key, self.first)
        

class BinarySearchST():
    def __init__(self):
        self.keys = []
        self.vals = []
        self.N = 0
        
    def size(self):
        return self.N
    
    def isEmpty(self):
        return(self.N == 0)
    
    
    def rank(self, key, lo, hi):
        if(hi < lo): return lo
        mid = int(lo + ( hi - lo)/2)
        if (key < self.keys[mid]): 
            return(self.rank(key, lo, mid))
        elif(key > self.keys[mid]):
            return(self.rank(key, mid+1, hi))
        else:
            return(mid)
        
    def rank(self, key):
        hi = len(self.keys)
        lo = 0
        while (hi >= lo): 
            mid = int(lo + ( hi - lo)/2)
            if (key < self.keys[mid]): 
                hi = mid
            elif(key > self.keys[mid]):
                lo = mid + 1
            else:
                return(mid)
        return lo
    
    def get(self, key):
        if self.isEmpty(): return(None)
        i = self.rank(key, 0, len(self.keys))
        if(i<self.N and self.keys[i]== key):
            return(self.vals[i])
        return None
    
    def put(self, key, value):
        i = self.rank(key, 0, len(self.keys))
        if(i < self.N and self.keys[i] == key):
            self.vals[i] = value
        for j in range(self.N, i, -1):
            self.keys[j] = self.keys[j-1]
            self.values[j] = self.values[j-1]
        self.keys[i] = key
        self.values[i] = value
        self.N = self.N + 1
        
        
BSST = BinarySearchST()
BSST.keys = [1, 2, 3, 4, 5]
BSST.vals = ['A', "B", "C", "D", "E"]
BSST.N = 5

BSST.rank(2, 0, len(BSST.keys))
BSST.get(3)

SST = SequentialSearchST()
#SST.first = SequentialSearchST.Node("A", 111)
SST.put("A", 111)
SST.put("B", 112)

def main():
    ST = {"A": 10}
    ST["H"] =20
    
    for i, k in ST.items():
        print(i, k)
        print(ST[i])
        
    