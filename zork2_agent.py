import gym
import gym_hw1
from collections import deque

class Node:
    def __init__(self, state, parent, path_cost):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

def bfs(initialState, graph, goal1, goal2, goal3):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    initialNode = Node(initialState, None, 0)
    frontier = deque([initialNode])
    explored = set()

    control1 = True
    control2 = True
    count = 0
    collected = 0
    arr = []
    while frontier:

        stateNode = frontier.popleft()

        explored.add(stateNode)

        if goal1 == graph[stateNode.state[0]][stateNode.state[1]]:
                for t in path(stateNode):
                    if graph[t[0]][t[1]] == 'T':
                        if not t in arr:
                            collected = collected + 1
                            arr.append(t)
                if (collected > goal2 and stateNode.path_cost >= 3/4*goal3 and stateNode.path_cost + collected <= goal3):
                    return stateNode


        collected = 0


        for i in range(4):
            cr = [stateNode.state[0]+ dr[i], stateNode.state[1] + dc[i]]
            if cr[0] < 0 or cr[1] < 0 or cr[0] >= len(graph[0]) or cr[1] >= len(graph[1]):
                continue


            neighborNode =  Node(cr, stateNode, stateNode.path_cost + 1)

            for  k  in frontier:
                if k.state == neighborNode.state:
                    control1 = False


            for k in explored:
                if k.state == neighborNode.state:
                    control2 = False


            if (control1 and control2):
                frontier.append(neighborNode)


            control1 = True
            control2 = True



            if (not frontier):
                count = count + 1
                bar = explored.copy()
                for k in bar:
                    countT = 0
                    countE = 0
                    for n in path(k):
                        if (graph[n[0]][n[1]] == 'T'):
                            countT = countT + 1
                        if (graph[n[0]][n[1]] == 'E'):
                            countE = countE + 1

                        if (countT == count and countE == 0):

                            while k:
                                if (graph[k.state[0]][k.state[1]] == 'T'):
                                    frontier.append(k)

                                k = k.parent

                explored.clear()
                arr.clear()

    return None

def path(node):
    path_back = []

    while node:
        path_back.append(node.state)
        node = node.parent
    return list(reversed(path_back))

def run_agent():
    # create the Gym environment
    env = gym.make('zork2-v0')
    env.reset()
    minTreasure = env.min_treasure()
    maxTurn = env.max_turn()
    t = 1
    control = True

    print('Dummy escape agent that always moves up')
    print('I need minimum',env.min_treasure(),'treasures to go home.')
    print('I have maximum',env.max_turn(),'action turns.')
    while True:
        env.render()    # you can used this for printing the environment

        # sense
        s = env.look()
        l = env.loc()

        # think
        # ...

        # act
        if (control):
            k = bfs(l, s, 'E', minTreasure,maxTurn)
            x = path(k)
            control = False


        # act
        # print(l[0]);
        if (s[l[0]][l[1]] == 'E'):
            break
        elif (s[l[0]][l[1]] == 'T'):
            ob, rew, done = env.step(env.ACTION_COLLECT)
            t = t - 1
        elif (x[t][0] > l[0]):
            ob, rew, done = env.step(env.ACTION_DOWN)
        elif (x[t][0] < l[0]):
            ob, rew, done = env.step(env.ACTION_UP)
        elif (x[t][1] < l[1]):
            ob, rew, done = env.step(env.ACTION_LEFT)
        elif (x[t][1] > l[1]):
            ob, rew, done = env.step(env.ACTION_RIGHT)
        t = t + 1


        if done:
            break


    env.close()


if __name__ == "__main__":
    run_agent()

