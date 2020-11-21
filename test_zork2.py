import zork2_agent
from gym.envs.registration import register
import gym.envs

del gym.envs.registry.env_specs['zork2-v0']

register(
    id='zork2-v0',
    entry_point='gym_hw1.envs:Zork2Env',
    kwargs={'desc': [
        "T...T...",
        "........",
        "........",
        ".....T.T",
        "........",
        "T.......",
        "......E.",
        "T...S.T."
        ], 'mintreasure':2, 'maxturn':100
    }
)

zork2_agent.run_agent()

