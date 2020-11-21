import gym
import gym_hw1



def run_agent():
    # create the Gym environment
    env = gym.make('escape-v0')
    env.reset()
    rows = len(env.look()[0])
    columns = len(env.look()[1])
    rowL = -1
    colL = -1
    rowK = -1
    colK = -1
    isLightOn = False
    for i in range(rows):
        for j in range(columns):
            if (env.look()[i][j] is 'L'):
                rowL = i
                colL = j

    print('Dummy escape agent that always moves up')
    while True:
        env.render()    # you can used this for printing the environment

        # sense
        s = env.look()




        l = env.loc()

        # think
        # ...

        # act

        if(l[0] == rowL and l[1] == colL):
            isLightOn = True
            for i in range(rows):
                for j in range(columns):
                    if (env.look()[i][j] is 'F'):
                        rowK = i
                        colK = j


        if (not isLightOn):
            if(l[0] > rowL):
                ob, rew, done = env.step(env.ACTION_UP)

            elif(l[0] < rowL):
                ob, rew, done = env.step(env.ACTION_DOWN)

            elif(l[1] > colL):
                ob, rew, done = env.step(env.ACTION_LEFT)

            elif (l[1] < colL):
                ob, rew, done = env.step(env.ACTION_RIGHT)

        else:
            if(l[0] > rowK and l[1] == colK):
                ob, rew, done = env.step(env.ACTION_UP)
            elif (l[1] < colK):
                ob, rew, done = env.step(env.ACTION_RIGHT)

            elif (l[1] > colK):
                ob, rew, done = env.step(env.ACTION_LEFT)


            elif (l[1] == colK):
                ob, rew, done = env.step(env.ACTION_UP)


        if done:
            break

    env.close()


if __name__ == "__main__":
    run_agent()

