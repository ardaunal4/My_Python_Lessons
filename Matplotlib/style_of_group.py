from matplotlib import pytplot as plt 

print(plt.style.available)

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dey_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75730, 83640]
plt.plot(ages_x, py_dey_y, color = 'b', linewidth = 3, label = 'Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68475, 68746, 74583]
plt.plot(ages_x, js_dev_y, color = 'r', linewidth = 3, label = 'JavaScript')
