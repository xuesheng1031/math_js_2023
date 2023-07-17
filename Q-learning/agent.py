import numpy as np
import random
from collections import deque
import pickle

class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay_rate=0.001):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = np.zeros((num_states, num_actions))
        self.replay_buffer = deque(maxlen=10000)

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, self.num_actions - 1)  # explore
        else:
            return np.argmax(self.q_table[state])  # exploit

    def learn(self, state, action, reward, next_state):
        self.replay_buffer.append((state, action, reward, next_state))
        if len(self.replay_buffer) > 1000:
            state, action, reward, next_state = random.choice(self.replay_buffer)
            q_next = np.max(self.q_table[next_state])
            q_target = reward + self.discount_factor * q_next
            q_delta = q_target - self.q_table[state][action]
            self.q_table[state][action] += self.learning_rate * q_delta
            self.exploration_rate *= (1 - self.exploration_decay_rate)

    def save_model(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            self.q_table = pickle.load(f)

    # Other methods as needed
