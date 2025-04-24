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
    final_qpos = None
    final_qvel = None

    for episode in range(n_episodes):
        if final_qpos is None:
            state = env.reset()
        else:
            env.reset()
            env.set_state(final_qpos, final_qvel)
            state = env._get_obs()  # Or env.get_obs() depending on your implementation

        done = False
        while not done:
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)
            if render:
                env.render()

        # Save simulator state (qpos and qvel)
        final_qpos = env.sim.data.qpos.copy()
        final_qvel = env.sim.data.qvel.copy()

        print(f"Episode {episode} ended.")

if __name__ == '__main__':
    main()
