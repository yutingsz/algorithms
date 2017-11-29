# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 23:11:18 2017

@author: Ting Yu Dell
"""

class TrieST():
    def __init__(self):
        
        self.root = None
    
    class Node():
        def __init__(self):
            self.R = 256
            self.val = None
            self.next = [self] * self.R
        
        def get(self, c):
            for i in range(0, self.R):
                if c == self.next[i].val:
                    return(i)
    
    def get_main(self, key):
        x = self.get(self.root, key, 0)
        if x == None:
            return(None)
        return(x.val)
        
    def get(self, x, key, d):
        if x == None:
            return(None)
        if d == len(key):
            return(x)
        c = key[d]
        return(self.get(x.next[x.get(c)], key, d+1))


    def put_main(self, key, val):
        self.root = self.put(self.root, key, val, 0)
        
    def put(self, x, key, val, d):
        if x == None:
            x = self.Node()
        if d == len(key):
            x.val = val
            return(x)
        c = key[d]
        x.next[x.get(c)] = self.put(x.next[x.get(c)], key, val, d+1)
        return(x)
        
        
tries_case = TrieST()

tries_case.put_main("Abc", 2)





class TST():
    def __init__(self): 
        self.root = None
    
    class Node():
        def __init__(self):
            self.c= None
            self.val = None
            self.left = None
            self.mid = None
            self.right = None
        
    def get_main(self, key):
        x = self.get(self.root, key, 0)
        if x == None:
            return(None)
        return(x.val)
        
    def get(self, x, key, d):
        if x == None:
            return(None)
        c = key[d]
        if c < x.c:
            return(self.get(self.left, key, d))
        elif c > x.c:
            return(self.get(self.right, key, d))
        elif d < len(key) - 1:
            return(self.get(self.mid, key, d+1))
        else: 
            return(x)


    def put_main(self, key, val):
        self.root = self.put(self.root, key, val, 0)
        
    def put(self, x, key, val, d):
        c = key[d]
        if x == None:
            x = self.Node()
            x.c = c
        if c < x.c:
            x.left = self.put(x.left, key, val, d)
        elif c > x.c:
            x.right = self.put(x.right, key, val, d)
        elif d < (len(key) - 1):
            x.mid = self.put(x.mid, key, val, d+1)
        else: 
            x.val = val
        return(x)
        
        
tries_case = TST()

tries_case.put_main("Abc", 2)