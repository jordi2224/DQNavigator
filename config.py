'''ENVIRONMENT VARIABLES'''
map_size = 2000
# Scene limit size
SLS = 2200
# Robot parameters
bounding_box_length = 500
bounding_box_width = 300
speed = 80
lat_speed = 0.15
MAX_RAY_DIST = 1.42 * SLS
# Display settings
collision_marker_size = 5
scale = 0.16
dx = -200
dy = -200
win_H = 650
win_W = 650

'''ENVIRONMENT REWARDS'''
STEP_REWARD = -1
BACKWARDS_MOVE_REWARD = -5
FORWARD_MOVE_REWARD = 1 # not in use
NO_MOVE_REWARD = -4
WALL_HIT_REWARD = -100
NO_STEPS_REWARD = -100
GOAL_REWARD = 150
TURN_TOWARDS_GOAL_REW = 2

'''NEURAL NET HYPERPARAMETERS'''
lr = 0.001
MAX_STEPS = 25
EPISODES = 10000 #2_000
DISPLAY_EVERY = 10
MIN_REPLAY_MEMORY_SIZE = 1_000
REPLAY_MEMORY_SIZE = 5_000
MINIBATCH_SIZE = 32
DISCOUNT = 0.99
CONVERGE_EVERY = 12
TRAIN_EVERY = 2
# Exploration settings
DEF_EPSILON = 1
EPSILON_DECAY = 0.99975
MIN_EPSILON = 0.001


ENABLE_RENDER = True
AGGREGATE_EVERY = 50