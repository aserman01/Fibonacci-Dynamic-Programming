# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:37:02 2023

@author: Admin
"""
import time

start = time.process_time()

def F(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return F(n-1) + F(n-2)
    

# print(F(45))
# print(time.process_time() - start)
# Took 311.640625 seconds, found 1134903170

def F_b(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        a = 0
        b = 1
        n = n-1
        
        while n > 0:
            c = a + b
            a = b
            b = c
            
            n -= 1
    
    return b


# print(F_b(45))
# print(time.process_time() - start)
# Took 0.0 seconds, found 1134903170

Fib_num = [-1]*100
def F_t(n):
    if Fib_num[n] == -1:
        if n == 0:
            Fib_num[n] = 0
    
        elif n == 1:
            Fib_num[n] = 1
        
        else:
            Fib_num[n] = F_t(n-1) + F_t(n-2)
            
    return Fib_num[n]
    
    
# print(F_t(45))
# print(time.process_time() - start)
# Took 0.0 seconds, found 1134903170 
   
    