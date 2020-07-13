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
STEP_REWARD = -2
BACKWARDS_MOVE_REWARD = -1
FORWARD_MOVE_REWARD = 4
NO_MOVE_REWARD = -25
WALL_HIT_REWARD = -400
NO_STEPS_REWARD = -1000 # -2000
GOAL_REWARD = 1000
TURN_TOWARDS_GOAL_REW = 8
TURN_AWAY_GOAL_REW = -2

'''NEURAL NET HYPERPARAMETERS'''
lr = 0.002
MAX_STEPS = 100
EPISODES = 4000  # 2_000
DISPLAY_EVERY = 15
MIN_REPLAY_MEMORY_SIZE = 1000  # 1_000
REPLAY_MEMORY_SIZE = 5000  # 5_000 @ About 60 episodes
MINIBATCH_SIZE = 64  # GREATLY affects performance
DISCOUNT = 0.98
CONVERGE_EVERY = 50
TRAIN_EVERY = 10
# Exploration settings
DEF_EPSILON = 1
EPSILON_DECAY = 0.9996
MIN_EPSILON = 0.03

ENABLE_RENDER = True
AGGREGATE_EVERY = 10

DEF_GAC = 0.2
GAC_DECAY = 1.0004
MAX_GAC = 0.85
DO_GAC = True

BENCHMARK_LENGTH = 50
BENCHMARK_EVERY = 100

'''PREPROCESSING CONFIG'''
RESOLUTION = bounding_box_length * 0.75  # to avoid collisions increase



