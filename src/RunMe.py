from main.Maze import Maze
from main.Agent import Agent
from main.mysolution.MyQLearning import MyQLearning
from main.mysolution.MyEGreedy import MyEGreedy
import os.path

if __name__ == "__main__":
    # load the maze
    file_toy_maze = "..\\..\\data\\toy_maze.txt"
    file_easy_maze = "..\\..\\data\\easy_maze.txt"
    maze = Maze(file_toy_maze)
    reward_toy_maze = maze.get_state(9, 9)
    # reward_easy_maze = maze.get_state(24, 14)

    # Set the reward at the bottom right to 10
    maze.set_reward(reward_toy_maze, 10)
    # Set second reward at the top right to 5
    reward_toy_maze_second = maze.get_state(9, 0)
    maze.set_reward(reward_toy_maze_second, 5)

    # create a robot at starting and reset location (0,0) (top left)
    robot = Agent(0, 0)

    # make a selection object (you need to implement the methods in this class)
    selection = MyEGreedy()

    # make a Q-learning object (you need to implement the methods in this class)
    learn = MyQLearning()

    trials = 0
    # total steps per all finished trials
    steps_trials = 0

    stop = False
    steps = 0
    steps_trial = 0

    epsilon = 1

    # keep learning until you decide to stop
    while not stop:
        action = selection.get_egreedy_action(robot, maze, learn, epsilon)

        state = robot.get_state(maze)
        robot.do_action(action, maze)

        state_next = robot.get_state(maze)
        possible_actions = maze.get_valid_actions(robot)
        reward = maze.get_reward(state_next)

        learn.update_q(state, action, reward, state_next, possible_actions, 0.7, 0.9)

        if reward == 10 or reward == 5:
            # print(reward)
            robot.reset()
            trials += 1
            if trials <= 10:
                steps_trials += steps_trial
            steps_trial = 0
            if reward == 10:
                epsilon = epsilon*0.95
            else:
                epsilon = epsilon*0.999

        steps += 1
        steps_trial += 1
        if steps == 30000:
            stop = True
