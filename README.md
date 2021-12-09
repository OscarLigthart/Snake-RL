# Snake-RL
A self-learning pygame implementation of Snake using Reinforcement Learning.

It consists of two major components:
- A python package consisting of a basic Snake game built on pygame.
- Reinforcement learning experiments in which agents learn to play this Snake game

## Setup

Start by creating the conda environment required to run the application.
```
conda env create -f environment.yml
```

Now that the environment has been build, you can make the application by running:
```
make
```

## Play the game

Now that you have built the application, you can play it simply by using the following command:
```
python -m snake_gym
```

## Run the RL experiments

You can start the training of the RL experiment by running:
```
python RL/train.py
```
