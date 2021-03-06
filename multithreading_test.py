import sys
import numpy as np
from tqdm import tqdm
from navigation.environment import Environment
from GUI_new_model_training import DQNAgent
import config as cfg
import math

if __name__ == '__main__':
    ini_lr = float(sys.argv[1])
    end_lr = float(sys.argv[2])
    N = int(sys.argv[3])
    step = math.fabs(ini_lr-end_lr)/N
    for i in range(N+1):
        lr = ini_lr+i*step
        print(lr)

        env = Environment()
        agent = DQNAgent(lr)
        episode_reward_history = []
        average_reward_history = []
        epsilon = cfg.DEF_EPSILON

        for episode in tqdm(range(6000), unit='sims'):

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
