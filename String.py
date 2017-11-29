# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:13:22 2017

@author: yuti
"""

a = ["Odk73gw", "Ab89dTe"]
import copy

class LSD():
    def sort(self, a, W):
        N= len(a)
        R =256
        for d in range(W-1, -1, -1):
            aux = copy.deepcopy(a)
            count_list = [0] * (R+1)
            for i in range(0, N, 1):
                count_list[ord(a[i][d])+1] = count_list[ord(a[i][d])+1] + 1
                
            for r in range(0, R, 1):
                count_list[r+1] = count_list[r]+ count_list[r+1]
            
            for i in range(0, N, 1):
                aux[count_list[ord(a[i][d])]] = a[i]
                count_list[ord(a[i][d])] = count_list[ord(a[i][d])] + 1
                
            for i in range(0, N, 1):
                a[i] = aux[i]
                
                

LSD_Case = LSD()


LSD_Case.sort(a, 7)


N= len(a)
W = 7
d = 6
N= len(a)
R =256


aux = copy.deepcopy(a)
count_list = [0] * (R+1)
for i in range(0, N, 1):
    count_list[ord(a[i][d])+1] = count_list[ord(a[i][d])+1] + 1
    
for r in range(0, R, 1):
    count_list[r+1] = count_list[r]+ count_list[r+1]

for i in range(0, N, 1):
    print(a[i][d])
    aux[count_list[ord(a[i][d])]] = a[i]
    count_list[ord(a[i][d])] = count_list[ord(a[i][d])] + 1
    
for i in range(0, N, 1):
    a[i] = aux[i]