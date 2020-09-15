import random


class MyEGreedy:

    def __init__(self):
        print("Made EGreedy")

    def get_random_action(self, agent, maze):
        # agent.do_action(self, random.choice(actions), maze)
        move = random.choice(maze.get_valid_actions(agent))
        return move

    def get_best_action(self, agent, maze, q_learning):
        actions = maze.get_valid_actions(agent)
        results = q_learning.get_action_values(agent.get_state(maze), actions)

        highest_q = max(results)
        best_action = []
        for i, result in enumerate(results):
            if result == highest_q:
                best_action.append(i)

        return actions[random.choice(best_action)]


    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        if random.uniform(0, 1) < epsilon:
            return self.get_random_action(agent, maze)
        else:
            return self.get_best_action(agent, maze, q_learning)
