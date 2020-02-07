# YET ANOTHER TRAINING ALGORITHM
from keras import Sequential
from keras.layers import Dense, InputLayer
from matplotlib import pyplot

from environment import Environment
from tqdm import tqdm
import numpy as np

env = Environment(diff='hard')

model = Sequential()
model.add(InputLayer(batch_input_shape=(1, env.STATE_SIZE)))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(env.ACTION_SIZE, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

DISCOUNT = 0.95
epsilon = 0.5
EPSILON_DECAY = 0.999

EPISODES = 1000

r_avg_list = []
for i in tqdm(range(EPISODES), unit='sims'):

    done, state, __ = env.reset()

    epsilon *= EPSILON_DECAY

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

        model.fit(np.array(state).reshape(-1, env.STATE_SIZE), target_vector.reshape(-1, env.ACTION_SIZE), epochs=1, verbose=0)
        state = new_state

        episode_reward += reward
        #env.render()

    r_avg_list.append(episode_reward/steps)

pyplot.plot(r_avg_list)
pyplot.title('Episode reward average')
pyplot.show()