import matplotlib.pyplot as plt

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = [60, 65, 60, 50, 55, 40, 30, 35, 40, 40]
plt.xlabel('No_of_Students enrolled')
plt.ylabel('marks')
plt.bar(c,v,color='maroon')
plt.show()
