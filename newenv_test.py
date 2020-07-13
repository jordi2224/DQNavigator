import random

import numpy as np
import pygame
from tqdm import tqdm
from navigation.environment import Environment
from GUI_new_model_training import DQNAgent

if __name__ == "__main__":

    env = Environment(diff='hard')
    env.render()
    agent = DQNAgent()
    while True:
        print("User's turn!")
        for episode in tqdm(range(20), unit='sims'):
            reward, state, done = env.reset()
            episode_reward = 0
            done = False
            while not done:
                pygame.time.wait(100)
                action = 5
                while action == 5:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[pygame.K_w]:
                        action = 2
                    elif pressed_keys[pygame.K_s]:
                        action = 3
                    elif pressed_keys[pygame.K_d]:
                        action = 0
                    elif pressed_keys[pygame.K_a]:
                        action = 1
                    else:
                        action = 5

                    # action = random.randrange(5)
                reward, new_state, done = env.step(action)
                print(reward)
                agent.update_replay_memory((state, action, reward, new_state, done))
                agent.train(done)

                state = new_state

                episode_reward += reward
                env.render()
            print("Episode done, reward: ", episode_reward)
            episode_reward = 0

        print("User's turn done")
        print("Time to test the NN!")
        N = 20
        total_reward = 0
        episode_reward = 0
        for episode in tqdm(range(N), unit='sims'):

            # Episode initialization
            episode_reward = 0
            reward, state, done = env.reset()
            done = False
            step = 0

            while not done:
                step += 1
                action = np.random.randint(0, env.ACTION_SIZE)

                # New environment state
                reward, new_state, done = env.step(action)
                episode_reward += reward

                # Show current state
                env.render()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                # Update memory and training
                agent.update_replay_memory((state, action, reward, new_state, done))
                agent.train(done)

                state = new_state

            total_reward += episode_reward
        print("AI's avg score: ", total_reward/N)