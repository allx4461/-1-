import generators as gn
import search as sc
import matplotlib.pyplot as plt
import time
timeline=[]
res1=[]
res2=[]
res3=[]
res4=[]
res5=[]
time_binpoisk=[]
time_pointers=[]
time_exponent=[]
time_binrazdel=[]
for l in range(100,5000,10):
    [m1,m2]=gn.generate_fortest(l)
    timeline.append(l)
    time_1=time.time()
    sc.two_pointers(m1,m2)
    time_2=time.time()
    sc.bin_perebor(m1,m2,0,l-1)
    time_3=time.time()
    sc.exppoisk(m1,m2)
    time_4=time.time()
    sc.binsmallermassive(m1,m2)
    time_5=time.time()

    res1.append((time_2-time_1)*100)
    res2.append((time_3 - time_2)*100)
    res3.append((time_4 - time_3)*100)
    res4.append((time_5 - time_4)*100)


fig, ax = plt.subplots()
plt.title('четные и нечетные')
plt.xlabel('size')
plt.ylabel('time')
ax.plot(timeline, res1, label="two_pointers")
ax.plot(timeline, res2, label="bin_split")
ax.plot(timeline, res3, label="exppoisk")
ax.plot(timeline, res4, label="bin_smaller")
ax.legend()

plt.show()
