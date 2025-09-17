# Tic-Tac-Toe AI – Project

This project was developed as a part of the **Artificial Intelligence** course at Dalarna University. It focuses on building an AI agent capable of playing the classic game **Tic-Tac-Toe** optimally against a human player.

---

## Goal

Create an intelligent agent that can play Tic-Tac-Toe and make decisions that are either:
- unbeatable (perfect play using Minimax), or
- adaptive (using reinforcement learning like Q-learning), or
- rule-based (heuristic strategy)

---

## Features

- Turn-based 3x3 grid implementation of the game
- AI agent makes moves based on implemented strategy
- Detection of:
  - Wins
  - Draws
  - Valid/invalid moves
- Optional: Human vs. AI or AI vs. AI mode

---

## AI Logic (Strategy Used)

- **Minimax Algorithm**:  
  The agent recursively explores all possible future moves and chooses the one that maximizes its chance of winning while minimizing the opponent's.

  OR

- **Q-Learning**:  
  The agent learns the value of different game states through trial and error using a Q-table.

  OR

- **Rule-based Heuristics**:  
  The agent follows predefined rules such as “take center if available”, “block opponent’s winning move”, etc.

---

## Technologies

- Python 3.x
- Jupyter Notebook
- `numpy`, `random`, (optional `matplotlib` for visualization)

---

## What I Learned

- How to represent game state and decision trees
- Implementing turn-based logic in Python
- Applying AI strategies like Minimax or Q-learning in real scenarios
- Using Jupyter Notebooks to combine explanation, code, and results in one place

---

## Status

- Fully functional  
- AI plays optimally (or improves over time if RL-based)  
- Demonstration video available (optional)

---

> This project showcases applied AI in a game setting and demonstrates how algorithms can simulate intelligent decision-making in classic board games like Tic-Tac-Toe.
