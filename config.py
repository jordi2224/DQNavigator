def scale_calculator(SLS, win_H, win_W):
    win_S = min([win_W, win_H])

    return float(win_S) / SLS

'''ENVIRONMENT VARIABLES'''
map_size = 2000
# Scene limit size
SLS = 4200
# Robot parameters
bounding_box_length = 500
bounding_box_width = 300
speed = 80
lat_speed = 0.15
MAX_RAY_DIST = 1.42 * SLS
# Display settings
collision_marker_size = 5
win_H = 650
win_W = win_H
scale = scale_calculator(SLS, win_H, win_W) # 0.16
dx = -200
dy = -200


'''ENVIRONMENT REWARDS'''
STEP_REWARD = -1
BACKWARDS_MOVE_REWARD = -1
FORWARD_MOVE_REWARD = 4
NO_MOVE_REWARD = -25
WALL_HIT_REWARD = -1
NO_STEPS_REWARD = -2
GOAL_REWARD = 1
TURN_TOWARDS_GOAL_REW = 8
TURN_AWAY_GOAL_REW = -2

'''NEURAL NET HYPERPARAMETERS'''
lr = 0.001
MAX_STEPS = 65
EPISODES = 30_000  # 2_000
DISPLAY_EVERY = 5
MIN_REPLAY_MEMORY_SIZE = 200  # 1_000
REPLAY_MEMORY_SIZE = 300  # 5_000 @ About 60 episodes
MINIBATCH_SIZE = 4  # GREATLY affects performance
DISCOUNT = 0.995
CONVERGE_EVERY = 25
TRAIN_EVERY = 1
# Exploration settings
DEF_EPSILON = 1
EPSILON_DECAY = 0.99995
MIN_EPSILON = 0.001

ENABLE_RENDER = False
AGGREGATE_EVERY = 75
BENCHMARK_LENGTH = 20

'''PREPROCESSING CONFIG'''
RESOLUTION = bounding_box_length * 0.75  # to avoid collisions increase



