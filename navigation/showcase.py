import numpy as np
import matplotlib.pyplot as plt
from navigation.astart_test import do_Astar, get_neighbours, points_in_circle_np
from sklearn.cluster import DBSCAN

grid = np.rot90(np.genfromtxt('grid.csv', delimiter=',')[1:, 1:])[175:350, 200:400]
grid[grid != 0] = 255

image = np.full((grid.shape[0], grid.shape[1], 3), (255, 255, 255))
image[grid != 0] = (150, 150, 150)

start = (142, 108)
end = (34, 48)
image[start] = (0, 255, 0)
image[end] = (0, 255, 0)

fig = plt.figure()

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == 255:
            vicinity = points_in_circle_np((i, j), 4)
            for v in vicinity:
                if grid[v] != 255:
                    pass
                    grid[v] = 20
image[grid == 20] = (255, 220, 220)

path = do_Astar(grid, start, end)

if False:
    for p in path:
        image[p] = (0, 255, 0)

plt.imshow(image[:, :])

previous_delta = [0, 0]
turns = []
for i in range(len(path) - 1):
    p1 = path[i]
    p2 = path[i + 1]

    delta = [p1[0] - p2[0], p1[1] - p2[1]]
    if delta != previous_delta:
        turns.append([p1[0], p1[1]])

    previous_delta = delta

print("Before: ", len(turns))
turns.append([start[0], start[1]])
turns = np.array(turns)
x = np.transpose(turns)[0]
y = np.transpose(turns)[1]

clustering = DBSCAN(eps=2, min_samples=0).fit(turns)
n_clusters = len(set(clustering.labels_))
clusters = [turns[clustering.labels_ == i] for i in range(n_clusters)]

centers_x = []
centers_y = []

for cluster in clusters:
    #centers_x.append(np.average(np.transpose(cluster)[0]))
    #centers_y.append(np.average(np.transpose(cluster)[1]))
    centers_x.append(cluster[0][0])
    centers_y.append(cluster[0][1])

# centers_x.insert(0, end[0])
# centers_y.insert(0, end[1])
centers_x[0] = end[0]
centers_y[0] = end[1]

print("After: ", len(centers_x))

plt.plot(centers_y, centers_x, 'x-')
plt.show()
