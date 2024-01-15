# SOLVING PONG USING REINFORCEMENT LEARNING:

![PRI_214439429.webp](SOLVING%20PONG%20USING%20REINFORCEMENT%20LEARNING%20297deffec744444db1f12374b4f9f99c/PRI_214439429.webp)

**Introduction :**

The purpose of this game, as per the code provided, is to simulate a game of Pong. Pong is a classic arcade game where two players control paddles and try to hit a ball back and forth. The goal is to make the opponent miss the ball, thus scoring a point.

In this specific implementation, there are three modes of play:

1. `AgentAI vs AgentAI`: In this mode, two AI agents play against each other. The AI is implemented using a Q-learning algorithm, a type of reinforcement learning.
2. `AgentAI vs Human`: In this mode, a human player can play against the AI agent.
3. `AgentRL vs AgentRL`: In this mode, two AI agents using reinforcement learning play against each other.

The game also includes a function to plot the agent's accumulated reward versus the iteration, which can be used to visualize the learning progress of the AI agent.

**Reinforecement learning explanation:**

![Q_Learning_Header_336c3f8177.png](SOLVING%20PONG%20USING%20REINFORCEMENT%20LEARNING%20297deffec744444db1f12374b4f9f99c/Q_Learning_Header_336c3f8177.png)

**Files Structure :**

[4.0K]  ./
├── [4.0K]  venv/
├── [1.9K]  [agent.py](http://agent.py/)
├── [5.7K]  [game.py](http://game.py/)
├── [1.0K]  [main.py](http://main.py/)
├── [  37]  [README.md](http://readme.md/)
└── [ 272]  requirements.txt

[game.py](http://game.py/): This is the main game file. It contains the Game class which handles the game logic. The class has methods for initializing the game, animating the ball and the player (both human and AI), and restarting the ball. The play method is the main game loop.

[agent.py](http://agent.py/): This file contains the Q-learning class which is used for the AI player. The class has methods for calculating the reward, converting the center to the state, getting the action, and updating the state. The calculate_reward function is a helper function that calculates the reward based on the position of the bar and the ball. The centre_to_state function is another helper function that converts the center position to a state.

[main.py](http://main.py/): This is the entry point of the application. It contains the GameLearning class which initializes the game based on the mode (AI vs AI, AI vs Human, or AI vs AI with reinforcement learning). The begin playing method starts the game. The plot_agent_reward function is a helper function that plots the agent's accumulated reward vs. iteration.

**Usage** :

```python
# **********************************************************create a virtual environement********************************************************** 
python -m venv venv 

**# activate the virtual environement**
source venv/bin/activate

# installing requirements
pip install -r requirements.txt

**# run the main.py file**
python main mode_number

**# -> The number is a variable mode_number
# Usage: python main.py mode 
# 1. AgentRL vs AgentAI 
# 2. AgentRL vs Human 
# 3. AgentRL vs AgentRL** 
```