import pygame
import random
import numpy as np
import config as cfg
import matplotlib.pyplot as pyplot
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras import optimizers
from navigation.environment import Environment
from tqdm import tqdm
from collections import deque

env = Environment(diff='hard')


def create_model(lr=cfg.lr):
    # MODEL ARCHITECTURE
    model = Sequential()
    model.add(Dense(12, input_dim=env.STATE_SIZE))
    model.add(Dropout(0.1))
    model.add(Dense(8, activation='sigmoid'))
    model.add(Dense(env.ACTION_SIZE, activation='relu'))

    optimizer = optimizers.Adam(learning_rate=lr, beta_1=0.9, beta_2=0.999, amsgrad=False)
    print("learning rate is: ", lr)
    model.compile(loss='binary_crossentropy', optimizer=optimizer)

    return model


class DQNAgent:

    def __init__(self, lr=cfg.lr):
        ''' Current model
            This model is used to get actions
            This model is trained every episode and fluctuates greately
            Eventually this is converged with target_model
        '''
        #self.model = create_model(lr=lr)

        ''' Target model
            This model is used to smooth out variation in the training
            target_model is only trained every n episodes
            this reduces fluctuations
            This model is used to get future Qs
        '''
        #self.target_model = create_model(lr=lr)
        #self.target_model.set_weights(self.model.get_weights())
        # Counter to decide when to converge
        self.target_update_counter = 0

        # Replay memory
        self.replay_memory = deque(maxlen=cfg.REPLAY_MEMORY_SIZE)

    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)

    def train(self, terminal_state):
        # Avoid training with too few transitions in memory
        if len(self.replay_memory) < cfg.MIN_REPLAY_MEMORY_SIZE:
            return

        minibatch = random.sample(self.replay_memory, cfg.MINIBATCH_SIZE)

        # Transitions are of shape (state, action, reward, new_state, done)
        current_states = np.array([transition[0] for transition in minibatch])
        current_qs_list = self.model.predict(current_states)

        # Future Qs are predicted using the TARGET_model not CURRENT_model to avoid fluctuations
        new_current_states = np.array([transition[3] for transition in minibatch])
        future_qs_list = self.target_model.predict(new_current_states)

        states = []
        actions = []

        for index, (current_state, action_h, reward_h, new_current_state, done_h) in enumerate(minibatch):
            # If not a final move
            if not done_h:
                # Target model's prediction
                max_future_q = np.max(future_qs_list[index])
                # Reinforce or punish this move
                # Propagate future q to this q
                new_q = reward_h + cfg.DISCOUNT * max_future_q
            else:
                new_q = reward_h

            # Update Q value for given state
            current_qs = current_qs_list[index]
            current_qs[action_h] = new_q

            # And append to our training data
            states.append(current_state)
            actions.append(current_qs)

            # Use this training data to train the current model
            self.model.fit(np.array(states), np.array(actions),
                           batch_size=cfg.MINIBATCH_SIZE,
                           verbose=0,
                           shuffle=False)

        if terminal_state:
            self.target_update_counter += 1

        if self.target_update_counter >= cfg.CONVERGE_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

def benchmark_agent(agent, diff):
    total_reward = 0
    env = Environment(diff=diff)
    for episode in range (cfg.BENCHMARK_LENGTH):
        episode_reward = 0
        done = False
        reward, state, done = env.reset()

        while not done:
            tmp_state = np.array(state).reshape(-1, env.STATE_SIZE)
            prediction = agent.model.predict(tmp_state)
            action = np.argmax(prediction)

            reward, new_state, done = env.step(action)
            episode_reward += reward

        total_reward += episode_reward

    return total_reward/cfg.BENCHMARK_LENGTH



if __name__ == "__main__":

    agent = DQNAgent()
    agent.model = load_model('endmodel_retrained.model')
    agent.target_model = load_model('endmodel_retrained.model')
    #lr = cfg.lr*10
    lr = 0.0002
    optimizer = optimizers.Adam(learning_rate=lr, beta_1=0.9, beta_2=0.999, amsgrad=False)
    print("learning rate is: ", lr)
    agent.model.compile(loss='binary_crossentropy', optimizer=optimizer)
    agent.target_model = load_model('endmodel.model')
    print("EASY: Agent scorde an avg: ", benchmark_agent(agent, diff='easy'))
    print("HARD: Agent scorde an avg: ", benchmark_agent(agent, diff='hard'))
    episode_reward_history = []
    average_reward_history = []
    epsilon = 0.1
    cfg.EPSILON_DECAY = cfg.EPSILON_DECAY

    for episode in tqdm(range(cfg.EPISODES), unit='sims'):

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
                action = np.random.randint(0, env.ACTION_SIZE-1)
                '''if np.random.random() < gac:
                    if math.fabs(state[-3]) > 0.15:
                        if state[-3] > 0:
                            action = 1
                        else:
                            action = 0
                    else:
                        action = 2'''

            # New environment state
            reward, new_state, done = env.step(action)
            episode_reward += reward

            # Show current state
            if not (episode % cfg.DISPLAY_EVERY) and cfg.ENABLE_RENDER:
                env.render()
            elif cfg.ENABLE_RENDER:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

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

    agent.model.save('endmodel_retrained.model')
    pyplot.plot(average_reward_history)
    pyplot.title('Episode reward average')
    pyplot.show()
