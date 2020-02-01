import threading

import numpy as np
from matplotlib import pyplot
from tqdm import tqdm
from environment import Environment
from GUI_new_model_trining import DQNAgent
import config as cfg

if __name__ == '__main__':
    lr = float(input("LR: "))
    print(lr)
    env = Environment()
    agent = DQNAgent(lr)
    episode_reward_history = []
    average_reward_history = []
    epsilon = cfg.DEF_EPSILON

    for episode in tqdm(range(400), unit='sims'):

        # Episode initialization
        episode_reward = 0
        reward, state, done = env.reset()
        done = False
        step = 0

        while not done:
            step += 1

            # Make a decision based on epsilon
            if np.random.random() > epsilon:
                # Action/Prediction generation
                tmp_state = np.array(state).reshape(-1, env.STATE_SIZE)
                prediction = agent.model.predict(tmp_state)
                action = np.argmax(prediction)
            else:
                # Get random action
                action = np.random.randint(0, env.ACTION_SIZE)

            # New environment state
            reward, new_state, done = env.step(action)
            episode_reward += reward

            # Update memory and training
            agent.update_replay_memory((state, action, reward, new_state, done))
            if not episode % cfg.TRAIN_EVERY:
                agent.train(done)

            state = new_state

        episode_reward_history.append(episode_reward)

        # Decay epsilon
        if epsilon > cfg.MIN_EPSILON:
            epsilon *= cfg.EPSILON_DECAY
            epsilon = max(cfg.MIN_EPSILON, epsilon)

        if not episode % cfg.AGGREGATE_EVERY or episode == 1:
            avg = sum(episode_reward_history) / len(episode_reward_history)
            print("epsilon: ", epsilon, " avg: ", avg)
            average_reward_history.append(avg)
            episode_reward_history = []

    print(average_reward_history)
    myfile = open("model_lr_"+str(lr)+".txt", "w")
    for i in average_reward_history:
        myfile.write(str(i) + '\n')

    myfile.close()
