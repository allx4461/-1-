def two_pointers(m1,m2):
    i1,i2=0,0
    while i1<len(m1) and i2<len(m2):
        if m1[i1]<m2[i2]: i1+=1
        elif m1[i1]>m2[i2]: i2+=1
        else: return True
    return False

def binpoisk(m1,elem,s):
    l, r = s, (len(m1) - 1)
    while l <= r:
        mid = (l + r) // 2
        if elem == m1[mid]: return [True,0]
        elif elem>m1[mid]: l=mid+1
        elif elem<m1[mid]: r=mid-1
    return [False,l]
def binsmallermassive(m1,m2):
    s=0
    if len(m1)<len(m2):
        for i in range(len(m1)):
            if binpoisk(m2,m1[i],s)[0]: return True
            s=binpoisk(m2,m1[i],s)[1]
        return False
    else:
        for i in range(len(m2)):
            if binpoisk(m1,m2[i],s)[0]: return True
            s = binpoisk(m1, m2[i], s)[1]
        return False

def exp_search(arr, x, s):
    if s >= len(arr) or len(arr) <= 0: return [False, s]
    if arr[s] == x: return [True, s]
    i = 1
    n = len(arr)
    while i + s < n and arr[s + i] < x:
        i *= 2
    l = s + (i // 2)
    r = min(s + i, n - 1)
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return [True, mid]
        if arr[mid] < x: l = mid + 1
        else: r = mid - 1
    return [False, l]
def exppoisk(m1, m2):
    if len(m1) <= len(m2): small, big = m1, m2
    else:
        small, big = m2, m1
    idx = 0
    for x in small:
        r, idx = exp_search(big, x, idx)
        if r: return True
    return False
def binpoisk2(arr, elem, l, r):
    left, right = l, r
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            return True, mid
        elif arr[mid] < elem:
            left = mid + 1
        else:
            right = mid - 1
    return False, left
def binsplit(small, big, l1, r1, l2, r2):
    if l1 > r1 or l2 > r2:return False
    mid1 = (l1 + r1) // 2
    x = small[mid1]
    found, pos = binpoisk2(big, x, l2, r2)
    if found:return True
    left = binsplit(small, big, l1, mid1 - 1, l2, pos - 1)
    if left:return True
    right = binsplit(small, big, mid1 + 1, r1, pos, r2)
    return right
def start_binsplit(m1, m2):
    if len(m1) <= len(m2):small, big = m1, m2
    else:small, big = m2, m1
    return binsplit(small, big, 0, len(small) - 1, 0, len(big) - 1)
