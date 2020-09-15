from main.QLearning import QLearning


class MyQLearning(QLearning):

    def update_q(self, state, action, r, state_next, possible_actions, alfa, gamma):
        # TODO Auto-generated method stub
        q = self.get_q(state, action)
        next_q = max(self.get_action_values(state_next, possible_actions))
        new_q = q + alfa * (r + gamma * next_q - q)
        self.set_q(state, action, new_q)
        return new_q
