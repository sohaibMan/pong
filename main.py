import sys
import game as g
import matplotlib.pylab as plt
import numpy as np


# Function to plot agent's accumulated reward vs. iteration
def plot_agent_reward(rewards):
    plt.plot(np.cumsum(rewards))  # Plot cumulative sum of rewards
    plt.title('Agent Cumulative Reward vs. Iteration')  # Set plot title
    plt.ylabel('Reward')  # Set y-axis label
    plt.xlabel('Episode')  # Set x-axis label
    plt.show()  # Display the plot


# Class for game learning
class GameLearning:
    # Initialize the game based on the mode
    def __init__(self, mode):
        if mode == 1:
            self.game = g.Game('agentAI')  # AI vs AI mode
        elif mode == 2:
            self.game = g.Game('human')  # AI vs Human mode
        else:
            self.game = g.Game('agentRL')  # AI vs AI with reinforcement learning mode

    # Method to start the game
    def beginPlaying(self):
        self.game.play()  # Start the game


# Main function
if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("""
        Usage: python main.py mode
        1. AgentRL vs AgentAI
        2. AgentRL vs Human
        3. AgentRL vs AgentRL
        """)
        sys.exit(1)  # Exit the program if the number of arguments is incorrect

    # Access the command-line argument
    game_mode = int(sys.argv[1])  # Convert the argument to integer

    gl = GameLearning(game_mode)  # Initialize the game
    gl.beginPlaying()  # Start the game
