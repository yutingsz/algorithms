# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:28:17 2017
Algorithms, 4th Edition
3.3 Balanced Search Trees
Red–black trees
@author: yuti
"""

class RedBlackBST():
    def __init__(self): 
        self.root = None
        self.RED =  True
        self.BLACK = False
    
    class Node():
        def __init__(self, key, val, N, color):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.N = N
            self.color= color
    
    def isRed(self, x):
        if x ==None:
            return(False)
        return(x.color == self.RED)
    
    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return(x)

    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        x.N = h.N
        h.N = 1 + self.size(h.left) + self.size(h.right)
        return(x)
    
    def size(self, x):
        if x == None: 
            return(0)
        return(x.N)
    
    def get_main(self, key):
        return(self.get(self.root, key))
    
    def get(self, h, key): 
        if h == None:
            return(None)
        if key < h.key:
            return(self.get(h.left, key))
        if key > h.key:
            return(self.get(h.right, key))
        if key == h.key:
            return(h.val)
        
    
    def put_main(self, key, val):
        self.root = self.put(self.root, key, val)
        
    def put(self, h, key, val):
        if h == None:
            return(self.Node(key, val, 1, self.RED))
        
        if key < h.key: 
            h.left = self.put(h.left, key, val)
        elif key > h.key: 
            h.right = self.put(h.right, key, val)
        else: 
            h.val = val
        
        if self.isRed(h.right) and (not self.isRed(h.left)):
            h= self.rotateLeft(h)
            if h == None:
                print(h)
        if self.isRed(h.left) and self.isRed(h.left.left):
            h= self.rotateRight(h)
            if h == None:
                print(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColors(h)
            if h == None:
                print(h)
          

        h.N = 1 + self.size(h.left) + self.size(h.right)
        
        return(h)
    
    def flipColors(self, h):
        h.color = self.RED
        h.left.color= self.BLACK
        h.right.color= self.BLACK
        #return(h)
        
        
bst_case = RedBlackBST()

bst_case.put_main("t", 10)
bst_case.put_main("d", 30)
bst_case.put_main("c", 40)
bst_case.put_main("a", 11)
bst_case.put_main("e", 22)
bst_case.put_main("f", 3)
bst_case.get_main("f")
        
            
            
            