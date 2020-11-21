import escape_agent
from gym.envs.registration import register
import gym.envs

del gym.envs.registry.env_specs['escape-v0']

register(
    id='escape-v0',
    entry_point='gym_hw1.envs:EscapeEnv',
    kwargs={'desc':[                                                                   
      "XFXXX",                                                             
      ".....",                                                             
      "...L.",                                                             
      ".....",                                                             
      "...S."                                                              
]}
)

escape_agent.run_agent()

