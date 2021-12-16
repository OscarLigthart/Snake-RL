# Snake-RL
A self-learning pygame implementation of Snake using Reinforcement Learning.

Below you can find an example of an episode performed by a trained agent.

<img src="/docs/example.gif" alt="Episode of a trained agent"/>

It consists of two major components:
- A python package consisting of a basic Snake game built on pygame, completed with OpenAI gym wrapper.
- Reinforcement learning experiments using a simple DQN (Deep Q-Network) in which agents learn to play this Snake game

## Setup

Start by creating the conda environment required to run the application.
```
conda env create -f environment.yml
```

Now that the environment has been build, you can install the snake_gym package by running:
```
pip install snake_gym/
```

## Play the game

Now that you have built the application, you can play it simply by using the following command:
```
python -m snake_gym
```

## Reinforcement Learning experiment


You can start the training of the RL experiment by running:
```
python RL/train.py
```

Alternatively, you can simply run inference of the trained agent by running:
```
python RL/inference.py
```
