import matplotlib.pyplot as plt


x = range(1,13,1)
y1 = (-5, -3, 2, 11, 19, 22, 24, 22, 16, 8, 1, -3)
y2 = (-4, -3, 2, 9, 16, 20, 23, 21, 15, 8, 2, -1)
plt.plot (x, y1, 'g', label='Moscow', linewidth=2)
plt.plot(x, y2, 'c', label='Saint-Petersburg', linewidth=2)
plt.title('Average daytime temp in Moscow and SPb during the year')
plt.ylabel('Average temp in degree of C')
plt.xlabel('Month')
plt.legend()
plt.show()
plt.savefig(plt.jpg)

