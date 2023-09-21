
import random

class QLearningAgent:
    def __init__(self, action_space, learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0, exploration_decay_rate=0.995):
        self.action_space = action_space
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = {}  # Q-table to store Q-values for state-action pairs

    def choose_action(self, state):
        """Choose an action using ε-greedy exploration strategy."""
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.action_space)  # Choose a random action
        else:
            # Choose the action with the highest Q-value for the current state
            q_values = [self.q_table.get((state, action), 0) for action in self.action_space]
            return self.action_space[q_values.index(max(q_values))]

    def update_q_value(self, state, action, reward, next_state):
        """Update the Q-value for the given state-action pair based on the reward received and the max Q-value of the next state."""
        current_value = self.q_table.get((state, action), 0)
        next_max_value = max([self.q_table.get((next_state, next_action), 0) for next_action in self.action_space])
        new_value = current_value + self.learning_rate * (reward + self.discount_factor * next_max_value - current_value)
        self.q_table[(state, action)] = new_value

        # Decay exploration rate
        self.exploration_rate *= self.exploration_decay_rate

    def get_policy(self, state):
        """Get the best action for the given state based on the Q-values."""
        q_values = [self.q_table.get((state, action), 0) for action in self.action_space]
        return self.action_space[q_values.index(max(q_values))]

    def train(self, env, episodes):
        """Train the agent on the environment."""
        for episode in range(episodes):
            state = env.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done = env.step(action)
                self.update_q_value(state, action, reward, next_state)
                state = next_state
