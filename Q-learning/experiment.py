import matplotlib.pyplot as plt

class Experiment:
    def __init__(self, agent, environment):
        self.agent = agent
        self.environment = environment
        self.rewards = []

    def train(self, episodes):
        for episode in range(episodes):
            state = self.environment.reset()
            done = False
            while not done:
                action = self.agent.choose_action(state)
                next_state, reward, done = self.environment.step(action)
                self.agent.learn(state, action, reward, next_state)
                state = next_state
            if episode % 100 == 0:
                print(f'Episode {episode} finished')

    def test(self, episodes):
        total_rewards = 0
        for episode in range(episodes):
            state = self.environment.reset()
            done = False
            while not done:
                action = self.agent.choose_action(state)
                next_state, reward, done = self.environment.step(action)
                state = next_state
                total_rewards += reward
            self.rewards.append(total_rewards)
            if episode % 100 == 0:
                print(f'Episode {episode} finished, total rewards: {total_rewards}')

    def plot(self):
        plt.plot(self.rewards)
        plt.xlabel('Episode')
        plt.ylabel('Total Rewards')
        plt.show()

    def save_model(self, file_path):
        self.agent.save_model(file_path)

    def load_model(self, file_path):
        self.agent.load_model(file_path)
