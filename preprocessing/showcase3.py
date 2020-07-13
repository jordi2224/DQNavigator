import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from navigation.astart_test import do_Astar, points_in_circle_np


def path_to_mans(path, start, end):
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
        # centers_x.append(np.average(np.transpose(cluster)[0]))
        # centers_y.append(np.average(np.transpose(cluster)[1]))
        centers_x.append(cluster[0][0])
        centers_y.append(cluster[0][1])

    # centers_x.insert(0, end[0])
    # centers_y.insert(0, end[1])
    centers_x[0] = end[0]
    centers_y[0] = end[1]

    return centers_x, centers_y, turns


files = ['./sc_grids/grid10.png']
#files = [ './sc_grids/grid9.png']

for f in files:
    image = np.array(cv2.imread(f))
    grid = image[:,:,0]
    grid = np.abs(255-grid)

    #boundary
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x,y] > 150:
                nei = points_in_circle_np((x,y), 3)
                for n in nei:
                    if grid[n] < 150:
                        grid[n] = 20


    image[grid == 20] = (255, 190 ,190)
    print("done bounds")

    p1 = (300,300)
    p3 = (241, 389)
    p2 = (196, 245)

    path1 = do_Astar(grid, p1, p2)
    pth1_x, pth1_y, t1 = path_to_mans(path1, p1, p2)


    print("path1 complete")
    path2 = do_Astar(grid, p2, p3)
    pth2_x, pth2_y, t2 = path_to_mans(path2, p2, p3)
    for p in path2:
        #image[p] = (100, 255, 100)
        pass
    print("path1 complete")

    plt.figure()
    plt.ion()
    if f == files[-1]:
        plt.ioff()
    plt.imshow(image)

    plt.plot(pth1_y, pth1_x, 'x', ls = '--', linewidth = 1)
    #plt.scatter(pth2_y, pth2_x, s=1)
    #plt.scatter(np.transpose(t1)[0], np.transpose(t1)[1], s=1)
    plt.plot(pth2_y, pth2_x, 'x', ls = '--', linewidth = 1)
    plt.show()

