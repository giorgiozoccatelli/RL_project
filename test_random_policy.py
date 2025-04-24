import pdb
import gym
import numpy as np
from env.custom_hopper import *

def main():
    env = gym.make('CustomHopper-source-v0')

    print('State space:', env.observation_space)
    print('Action space:', env.action_space)
    print('Dynamics parameters:', env.get_parameters())

    use_saved_state = False
    final_qpos, final_qvel = None, None

    n_episodes = 500
    render = True

    for episode in range(n_episodes):
        if not use_saved_state:
            state = env.reset()
        else:
            env.set_state(final_qpos, final_qvel)
            env.sim.forward()
            state = env.get_obs()
            #print("Restored qpos:", final_qpos)
            #print("Restored qvel:", final_qvel)

        print(f"\n=== Episode {episode} START ===")
        print("Initial state:", state)

        done = False
        total_reward = 0.0

        while not done:
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
            total_reward += reward
            print(info)

            if render:
                env.render()

        final_qpos = env.sim.data.qpos.copy()
        final_qvel = env.sim.data.qvel.copy()
        use_saved_state = True  # Flip the switch after first episode

        print("Final state:", state)
        print("Total reward:", total_reward)
        print(f"=== Episode {episode} END ===")

if __name__ == '__main__':
    main()
