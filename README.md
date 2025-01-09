# Project 16: Pong Game

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 19 Dec 2024

## Description:
This is a Pong game implemented using Python's `turtle` and `time` modules with an object-oriented programming (OOP) approach. The game involves two players, left and right, competing to reach the winning score.

## How to Use:
1. Launch the game by running `app.py` (see the "Running the Program" section below).
2. Control the paddles:
   - **Left Paddle**: Press "W" to move up and "S" to move down.
   - **Right Paddle**: Press "O" to move up and "L" to move down.
3. The first player to reach a score of 10 wins the game.
4. When the game ends, a winning message is displayed. To play again, restart `app.py`.
5. Gameplay screenshots are stored in the `screenshots` folder within the project directory.

## Level
- **Level**: Intermediate
- **Skills**: OOP, Python Modules (`turtle`, `time`), Game Development
- **Domain**: Game Programming

## Features
- Dynamic ball speed: The ball's speed increases when it collides with a paddle and decreases when missed.
- Player controls for both left and right paddles.
- Scoreboard displaying current scores for both players.
- Winning message displayed when a player reaches 10 points.
- Game resets upon restart of `app.py`.
- Gameplay screenshots saved for reference.
- `experiments` folder contains temporary files or practice scripts.
- Project modified at different dates to improve functionality and design.

## Classes and Methods:
### `Ball`
- Creates and manages the ball's behavior.
- **Methods**:
  - `move()`: Moves the ball across the screen.
  - `bounce_y()`: Handles ball collision along the y-axis.
  - `bounce_x()`: Handles ball collision along the x-axis or paddles.
  - `reset_position()`: Resets the ball to the center and adjusts speed dynamically.

### `Paddle`
- Creates left and right paddles at specified locations.
- **Methods**:
  - Moves paddles up and down using assigned keys.

### `Scoreboard`
- Displays and updates scores for both players.
- **Methods**:
  - Updates the score when a paddle misses the ball.
  - `check_winner()`: Determines the winner and displays a message.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/pong-game-intermediate.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pong-game-intermediate
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

