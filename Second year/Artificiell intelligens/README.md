# Artificial Intelligence

This repository contains all lab assignments and deliverables from the course **Artificial Intelligence** at Dalarna University. The course covered a wide range of foundational AI techniques: from clustering and classification to pathfinding and reinforcement learning.

Each lab includes a Jupyter notebook or script.

---

## Course Labs Overview

### Lab 1 – Unsupervised Learning

- **Techniques**: k-Means and Agglomerative Clustering  
- **Tools**: `pandas`, `seaborn`, `matplotlib`, `scikit-learn`  
- **Tasks**:
  - Customer segmentation using k-means (`customerdata4.csv`)
  - Wholesale client segmentation with agglomerative clustering (`Wholesale customers dataset`)
- **Deliverables**: Jupyter notebooks with exploratory analysis, clustering logic, dendrograms, and cluster insights.

---

### Lab 2 – Supervised Classification Learning

- **Techniques**:  
  - k-Nearest Neighbors (k-NN)  
  - Decision Trees  
- **Dataset**: Custom-selected from [UCI ML Repository](https://archive.ics.uci.edu/)  
- **Experiments**:
  - 18 variations of k-NN with different values of *k*, normalization, and train-test splits
  - Accuracy tracking and confusion matrices  
  - Decision tree performance over 100 randomized runs
- **Deliverables**: Annotated notebooks and performance visualizations

---

### Lab 3 – Supervised Regression Learning

- **Goal**: Predict continuous values using regression models  
- **Techniques**: Linear Regression, Polynomial Regression  
- **Evaluation**: RMSE, R²-score, training/test split analysis  
- **Deliverables**: Jupyter notebook demonstrating regression models and comparisons

---

### Lab 4 – Pathfinding (A* Search Algorithm)

- **Goal**: Solve a maze by finding the shortest path using A*  
- **Algorithm**:  
  - `f(n) = g(n) + h(n)`  
  - Heuristic: Euclidean distance  
- **Tools**: Custom maze generator + visualization  
- **Deliverables**: A working pathfinding system

---

### Lab 5 – Reinforcement Learning with Q-Learning

- **Goal**: Train an agent to solve a maze using reinforcement learning  
- **Environment**: Maze represented as a 17x17 grid  
- **Algorithm**: Q-Learning  
  - Reward structure: `+1` for reaching the goal, `0` otherwise  
  - Optional: Reward decay and visualization of learning curve  
- **Deliverables**:
  - Annotated notebook
  - Plot showing improvement in agent's performance over epochs

---

## Tools & Libraries Used

- Python  
- Jupyter Notebook  
- Libraries: `numpy`, `matplotlib`, `pandas`, `seaborn`, `scikit-learn`, `heapq`  
- Optional visualizations: `pygame`, animations

---

## Learning Outcomes

- Apply clustering techniques for unsupervised learning tasks  
- Implement and evaluate classification algorithms for real datasets  
- Solve pathfinding problems using heuristic search (A*)  
- Understand and implement reinforcement learning with Q-learning  
- Practice scientific thinking through experimentation and performance evaluation

---

## Presentation Format

Each lab was demonstrated through:
- Discussion of implementation choices, results, and reflections

---

>  This folder showcases foundational AI concepts implemented from scratch, covering unsupervised learning, supervised learning, pathfinding, and reinforcement learning — all in Python and Jupyter.
