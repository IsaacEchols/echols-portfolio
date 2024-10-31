#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Using results from my dissertation, I wrote these functions to give the number of primitive periodic orbits of a given length in a circulant graph
#This code predates theorem 1 in our paper PERIODIC ORBITS ON 2-REGULAR CIRCULANT DIGRAPHS and uses theorem 2 instead.
#We generate sequences to search in OEIS
#For instance, fixing a and b and increasing n, searching for Orbits_up_to_n
#Another example, fixing a and b and increasing n, searching for Pl(n,a,b,n)
#I haven't found any matches so far, so let me know if you happen to go searching yourself and get a hit!  :)

from math import factorial

def binomial(x, y):
    try:
        return factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        return 0

#the set of common divisors of x,y
def CD(x,y):
    if x*y == 0:
        return [max(x,y)]
    List = []
    for i in range(1,min(x,y)+1):
        if x%i==y%i==0:
            List.append(i)
    return List        
    
def is_prime(x):
    if x < 2: 
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

#the set of common PRIME divisors of x,y
def CPD(x,y):
    List = CD(x,y)
    for i in CD(x,y):
        if is_prime(i) == False:
            List.remove(i)
    return List

#the set of b-counts k for which an orbit of length l exists on C_n(a,b)
def k_values(n,a,b,l):
    List = []
    for i in range(0,l+1):
        if (l*a + i*(b-a))%n == 0:
            List.append(i)
    return List

#the set of common prime divisors of x,y,z
def W(x,y,z):
    return CPD(max(CD(x,y)),z)


        
def Tailset(s):
    t = []
    for i in s:
        t.append(i)
    t.pop(0)
    return t


def Psetadd(oldpset,newitem):
    newset = []
    for i in oldpset:
        newset.append(i)
    for j in oldpset:
        c = j.copy()
        c.append(newitem)
        newset.append(c)
    return newset
        
#my version of the powerset
def Powerset(s):
    if len(s) == 0:
        return [[]]
    else:        
        scopy = s.copy()
        x = scopy[0]
        #print("x = " + str(x))
        scopy.pop(0)
        #print("x still = " + str(x))
        return Psetadd(Powerset(scopy),x)
    
#the product of elements in a finite set of numbers     
def Prod(s):
    result = 1
    for i in s:
        result = result*i
    return result 

#the number of primitive periodic orbits on C_n(a,b) of length l and b-count k
def plk(n,a,b,l,k):
    if (l*a + k*(b-a))%n != 0:
        return 0
    else:
        omega = int((l*a + k*(b-a))/n)
        print("omega = " + str(omega))
        w = W(l,k,omega)
        #print("W = " + str(w))
        result = 0
        for f in Powerset(w):
            result = result + ((-1)**(len(f)))*(binomial((l/Prod(f)),(k/Prod(f))))
        return int(result*(n/l))

#the number of primitive periodic orbits on C_n(a,b) of length l
def pl(n,a,b,l):
    result = 0
    for k in k_values(n,a,b,l):
        #print(k)
        result = result + plk(n,a,b,l,k)
    return result

#the number of orbits of length l 
def Orbits_up_to_n(n,a,b):
    result = 0
    for l in range(1,n+1):
        result = result + pl(n,a,b,l)
    return result

##################################################

x = plk(44,5,14,36,24)
print(x)

y = int((binomial(36,24)-binomial(12,8))*44/36)
print(y)

print(y-x)

print(pl())





