"""Test a random policy on the OpenAI Gym Hopper environment.

    
    TASK 1: Play around with this code to get familiar with the
            Hopper environment.

            For example:
                - What is the state space in the Hopper environment? Is it discrete or continuous?
                - What is the action space in the Hopper environment? Is it discrete or continuous?
                - What is the mass value of each link of the Hopper environment, in the source and target variants respectively?
                - what happens if you don't reset the environment even after the episode is over?
                - When exactly is the episode over?
                - What is an action here?
"""
import gym
from env.custom_hopper import *
import numpy as np

def main():
    env = gym.make("CustomHopper-source-v0")
    print('State space:', env.observation_space)
    print('Action space:', env.action_space)
    print('Dynamics parameters:', env.get_parameters())

    n_episodes = 500
    render = True

    for episode in range(n_episodes):
    if final_state is None:
        state = env.reset()
    else:
        env.reset()
        env.set_state(final_state)  # Inject the final state back into the env
        state = final_state

    done = False
    while not done:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        if render:
            env.render()

    final_state = state  # Save state even if done
    print(f"Episode {episode} ended.")

if __name__ == '__main__':
    main()

