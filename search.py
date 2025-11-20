import random

def two_pointers(m1,m2):
    i1,i2=0,0
    while i1<len(m1) and i2<len(m2):
        if m1[i1]<m2[i2]: i1+=1
        elif m1[i1]>m2[i2]: i2+=1
        else: return True
    return False

def binpoisk(m1,elem):
    l, r = 0, (len(m1) - 1)
    while l <= r:
        mid = (l + r) // 2
        if elem == m1[mid]: return True
        elif elem>m1[mid]: l=mid+1
        elif elem<m1[mid]: r=mid-1
    return False
def binsmallermassive(m1,m2):
    if len(m1)<len(m2):
        for i in range(len(m1)):
            if binpoisk(m2,m1[i]): return True
        return False
    else:
        for i in range(len(m2)):
            if binpoisk(m1,m2[i]): return True
        return False
def exp_search(arr, x):
    if not arr: return False
    if arr[0] == x: return True
    i = 1
    n = len(arr)
    while i < n and arr[i] < x:
        i *= 2
    l = i // 2
    r = min(i, n - 1)
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return True
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False
def exppoisk(m1,m2):
    if len(m1)<=len(m2): small,big=m1,m2
    else: small,big=m2,m1
    for x in small:
        if exp_search(big,x): return True
    return False
def bin_perebor(m1,m2):
    if len(m1)<1: return False
    return binpoisk(m2,m1[len(m1)//2]) or bin_perebor(m1[0:len(m1)//2],m2) or bin_perebor(m1[len(m1)//2+1:len(m1)],m2)
