import math
import numpy as np
import matplotlib.pyplot as plt


def points_in_circle_np(p, radius):
    x0, y0 = p
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:, np.newaxis] - x0) ** 2 + (y_ - y0) ** 2 <= radius ** 2)
    # x, y = np.where((np.hypot((x_-x0)[:,np.newaxis], y_-y0)<= radius)) # alternative implementation
    for x, y in zip(x_[x], y_[y]):
        yield x, y


def get_neighbours_one(p, shape):
    out = []
    for out_p in [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1),
                  (p[0] + 1, p[1] + 1), (p[0] - 1, p[1] - 1), (p[0] + 1, p[1] - 1), (p[0] - 1, p[1] + 1)]:
        if 0 <= out_p[0] < shape[0] and 0 <= out_p[1] < shape[1]:
            out.append(out_p)
    return out


def get_neighbours(p, shape, count=1):
    out = []
    out.extend(get_neighbours_one(p, shape))

    return out


def is_diagonal(p1, p2):
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return False
    else:
        return True


def do_Astar(grid, start, end):
    h = np.full(grid.shape, 9999)
    g = np.zeros(grid.shape)
    f = np.zeros(grid.shape)
    open_nodes = []
    close_nodes = []

    h[start] = 0
    # Add start node to open
    open_nodes.append(start)

    while True:
        # Select minimum open node
        min_f = float('Inf')
        min_index = (-1, -1)
        for n in open_nodes:
            if f[n] < min_f:
                min_f = f[n]
                min_index = n

        current = min_index
        # Remove current from OPEN
        open_nodes.remove(current)
        # Add current to CLOSED
        close_nodes.append(current)

        # Check if path is found
        if current == end:
            break

        # Check and calculate all neighbors
        for neighbour in get_neighbours(current, grid.shape):
            if grid[neighbour] != 0 or neighbour in close_nodes:
                continue
            else:
                if neighbour not in open_nodes:
                    open_nodes.append(neighbour)
                g_cost = int(math.sqrt(math.pow(neighbour[0] - end[0], 2) + math.pow(neighbour[1] - end[1], 2)) * 10)
                h_cost = h[current] + 14 if is_diagonal(current, neighbour) else h[current] + 10
                g[neighbour] = g_cost
                if h_cost < h[neighbour]:
                    h[neighbour] = h_cost

                f = g + h

    path = [end]
    current = end

    while current != start:
        possible = get_neighbours(current, grid.shape)
        for p in path:
            if p in possible:
                possible.remove(p)

        min_f = float('Inf')
        for n in possible:
            if h[n] < min_f:
                min_f = h[n]
                min_index = n

        path.append(min_index)
        current = min_index

    f[f > 2000] = 0
    h[h > 2000] = 0

    return path
