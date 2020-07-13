# YET ANOTHER TRAINING ALGORITHM
from keras import Sequential
from keras.layers import Dense, InputLayer
from matplotlib import pyplot

from navigation.environment import Environment
from tqdm import tqdm
import numpy as np
from keras.optimizers import Adam
from scipy import signal

env = Environment(diff='easy')
env.ACTION_SIZE -= 1

learning_rate = 0.02

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, env.STATE_SIZE)))
model.add(Dense(env.ACTION_SIZE, activation='linear'))
model.compile(loss='mse', optimizer=Adam(learning_rate = learning_rate), metrics=['mae'])

DISCOUNT = 0.75
epsilon = 1
EPSILON_DECAY = 0.99978

EPISODES = 300_000

r_avg_list = []
victory_counter = 0
for i in tqdm(range(EPISODES), unit='sims'):

    reward, state, __ = env.reset()

    epsilon *= EPSILON_DECAY
    done = False
    episode_reward = 0
    steps = 0
    while not done:
        steps += 1
        if np.random.random() < epsilon:
            action = np.random.randint(0, env.ACTION_SIZE)
        else:
            action = np.argmax(model.predict(np.array(state).reshape(-1, env.STATE_SIZE)))

        reward, new_state, done = env.step(action)
        target = reward + DISCOUNT * np.max(model.predict(np.array(new_state).reshape(-1, env.STATE_SIZE)))
        target_vector = model.predict(np.array(state).reshape(-1, env.STATE_SIZE))[0]
        target_vector[action] = target

        model.fit(np.array(state).reshape(-1, env.STATE_SIZE), target_vector.reshape(-1, env.ACTION_SIZE), epochs=1,
                  verbose=0)
        state = new_state

        episode_reward += reward

        #if not i % 10:
            #env.render()

    if reward > 1:
        victory_counter += 1

    if not i % 100:
        print(epsilon, " ", victory_counter)
        victory_counter = 0

    r_avg_list.append(episode_reward / steps)

pyplot.plot(signal.savgol_filter(r_avg_list, 1581, 3))
pyplot.title('Episode reward average')
pyplot.show()
np.savetxt('data.csv', r_avg_list, delimiter=',')