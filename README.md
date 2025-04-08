# TURTLE CROSSING GAME

A simple arcade-style game built using Python and Turtle graphics where the player controls a turtle trying to cross a busy road without getting hit by oncoming traffic. The game utilizes Object-Oriented Programming (OOP) to manage the player, cars, levels, and game logic.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

The Turtle Crossing Game is inspired by the classic "Frogger" game. The objective is to help the turtle reach the top of the screen while dodging moving cars. Each time the turtle succeeds, the level increases and the cars move faster. The game ends when the turtle collides with a car.

This project emphasizes clean code structure and reusability using OOP principles.

## How it Works

1. **Start the Game**: Run the `main.py` file.
2. **Controls**:
   - `w`: Move the turtle forward.
3. **Gameplay**:
   - Cars continuously move from right to left across the screen.
   - The turtle must reach the top without getting hit.
   - When the turtle reaches the top, it resets to the bottom and the level increases.
   - Car speed increases with each new level.
4. **Game Over**:
   - If the turtle collides with a car, a “Game Over” message is displayed and the game stops.

## Technologies Used

- **Python**: Programming language used for development
- **Turtle Graphics**: For rendering game visuals and animations
- **OOP (Object-Oriented Programming)**: To encapsulate game components like `Player_turtle`, `Carr`, and `Score`

## Lessons Learned

Through this project, I learned and applied:

- **Object-Oriented Design**: Separating responsibilities across different classes
- **Collision Detection**: Implementing proximity-based checks to detect turtle-car collisions
- **Dynamic Difficulty**: Increasing challenge level by accelerating car movement over time
- **Game Loop Management**: Using `time.sleep()` and continuous screen updates for real-time gameplay
- **Code Modularity**: Keeping logic clean and organized
