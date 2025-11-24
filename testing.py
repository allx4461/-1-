import generators as gn
import search as sc
import matplotlib.pyplot as plt
import numpy as np
import time
timeline=[]
res1=[]
res2=[]
res3=[]
res4=[]
time_binrazdel=[]
r=1
k=5
for l in range(10,1000,1):
    [m1,m2]=gn.generate_fortest(l,r)
    timeline.append(l)
    time_1=time.time()
    for i in range(k):sc.two_pointers(m1,m2)
    time_2=time.time()
    for i in range(k):sc.start_bin_perebor(m1,m2)
    time_3=time.time()
    for i in range(k):sc.exppoisk(m1,m2)
    time_4=time.time()
    for i in range(k):sc.binsmallermassive(m1,m2)
    time_5=time.time()

    res1.append((time_2-time_1))
    res2.append((time_3 - time_2))
    res3.append((time_4 - time_3))
    res4.append((time_5 - time_4))


fig, ax = plt.subplots()
plt.title('четные и нечетные (размер отличается в 1000 раз)')
plt.xlabel('size')
plt.ylabel('time')
plt.ylim([10**-5, 10**-2])
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
ax.plot(timeline, res1, label="two_pointers")
ax.plot(timeline, res2, label="bin_split")
ax.plot(timeline, res3, label="exppoisk")
ax.plot(timeline, res4, label="bin_smaller")
ax.legend()

plt.show()
