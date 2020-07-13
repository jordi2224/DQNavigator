import numpy as np

from driver.TSFinalDriver import Driver
import matplotlib.pyplot as plt

from preprocessing.wallsCV import doHoughTransform, translate_walls, exp_doHoughTransformP, lines_to_walls
from easy_comms import *

s = get_def_connection()
buff = ''

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=False, sharey=False)
fig.suptitle("Hough Transform\n")
x, y, buff = do_scan(s, buff, 1000, 5000)
ax1.scatter(x, y, s=1)

resolution_div = 40

walls, offset_x, offset_y, rhos_array, theta_array, clusters = doHoughTransform(x, y, resolution_div,
                                                                                remove_redundant=True)
walls = translate_walls(walls, offset_x, offset_y, resolution_div)

for wall in walls:
    ax1.plot([wall.start_x, wall.end_x], [wall.start_y, wall.end_y], alpha=1)


ax1.set_title("Standard HT")
ax2.set_title("Probabilistic HT")

x, y, buff = do_scan(s, buff, 1000, 5000)
ax2.scatter(x, y, s=1)


lines, offset_x, offset_y = exp_doHoughTransformP(x, y, resolution_div)

walls = lines_to_walls(lines)

walls = translate_walls(walls, offset_x, offset_y, resolution_div)
for wall in walls:
    ax2.plot([wall.start_x, wall.end_x], [wall.start_y, wall.end_y], c='k', alpha=0.7, linewidth=4)

plt.show()
