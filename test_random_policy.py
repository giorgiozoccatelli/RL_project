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

from env.custom_hopper import *


def main():
	env = gym.make('CustomHopper-source-v0')
	# env = gym.make('CustomHopper-target-v0')

	print('State space:', env.observation_space) # state-space
	print('Action space:', env.action_space) # action-space
	print('Dynamics parameters:', env.get_parameters()) # masses of each link of the Hopper

	n_episodes = 500
	render = True

	final_state = None  # To store the last state

	for episode in range(n_episodes):
	    if final_state is None:
	        state = env.reset()  # First episode requires reset
	    else:
	        state = final_state  # For subsequent episodes, use the final state
	    
	    done = False
	
	    while not done:
	        action = env.action_space.sample()  # Take a random action
	        state, reward, done, info = env.step(action)
	
	        # Save the final state for the next episode
	        if done:
	            final_state = state
	
	        # Optionally render the environment
	        env.render()


if __name__ == '__main__':
	main()
