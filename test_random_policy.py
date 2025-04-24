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
import pdb
import gym
import numpy as np
from env.custom_hopper import *

def main():
    env = gym.make('CustomHopper-source-v0')
    # env = gym.make('CustomHopper-target-v0')

    print('State space:', env.observation_space)
    print('Action space:', env.action_space)
    print('Dynamics parameters:', env.get_parameters())

    final_state = None
    n_episodes = 500
    render = True

    for episode in range(n_episodes):
        if final_state is None:
            state = env.reset()
        else:
            env.reset()
            env.set_state(final_qpos, final_qvel)
            state = env.get_obs()  # step to generate a new observation

        print(f"\n=== Episode {episode} START ===")
        print("Initial state:", state)

        done = False
        total_reward = 0.0

        while not done:
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
            total_reward += reward

            if render:
                env.render()

        final_qpos = env.sim.data.qpos.copy()
        final_qvel = env.sim.data.qvel.copy()

        print("Final state:", state)
        print("Total reward:", total_reward)
        print(f"=== Episode {episode} END ===")

if __name__ == '__main__':
    main()
