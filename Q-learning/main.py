from environment import Environment
from agent import QLearningAgent
from experiment import Experiment

def main():
    # Create the environment, agent, and experiment
    environment = Environment(...)
    agent = QLearningAgent(...)
    experiment = Experiment(agent, environment, ...)

    # Run the experiment
    experiment.train(episodes=...)
    experiment.test(episodes=...)

    # Plot the results
    experiment.plot()

if __name__ == "__main__":
    main()
