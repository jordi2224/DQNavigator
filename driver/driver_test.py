from driver.TSFinalDriver import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    driver = Driver("COM6")
    d_size = driver.start_scan_express()

    max_distance = 3000
    points, x, y = driver.get_point_cloud(920, max_distance)
    plt.rcParams.update({'font.size': 22})
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.scatter(x, y, s=1)
    ax1.axis([-max_distance, max_distance, -max_distance, max_distance])
    ax1.set_aspect('equal')

    points, x, y = driver.get_point_cloud(6000, max_distance)
    ax2.scatter(x, y, s=1)
    ax2.axis([-max_distance, max_distance, -max_distance, max_distance])
    ax2.set_aspect('equal')


    plt.show()
