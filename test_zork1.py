import zork1_agent
from gym.envs.registration import register
import gym.envs

del gym.envs.registry.env_specs['zork1-v0']

register(
    id='zork1-v0',
    entry_point='gym_hw1.envs:Zork1Env',
    kwargs={'desc': [
        "T...T...",
        "........",
        "........",
        ".....T.T",
        "........",
        "T.......",
        "......E.",
        "T...S.T."
        ], 'mintreasure':3
    }
)

zork1_agent.run_agent()

