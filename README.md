# Alien Invasion Game
Alien Invasion is a classic arcade-style game built using Python and the Pygame library. In this game, players control a spaceship to shoot down waves of aliens while avoiding collisions and managing their score. The game features dynamic difficulty adjustments, a scoring system, and various interactive elements to enhance gameplay.

1. Features
- Dynamic Gameplay: Control the spaceship to move left and right, and shoot bullets at incoming aliens.
- Game State Management: Track game statistics, score, and levels.
- Alien Fleet: Enemies move in formations and drop down the screen, increasing the challenge.
- Game Controls:
  - Arrow keys to move the spaceship.
  - Spacebar to shoot bullets.
  - 'Q' key to quit the game.
    
2. Installation
- Clone the repository
- Navigate to the project directory
- Install the required dependencies

3. Usage
Run the game by executing the alien_invasion.py file:

4. Code Overview
  - settings.py: Contains settings for the game, including screen dimensions, colors, and game speeds.
  - ship.py: Defines the player's spaceship and its movements.
  - bullet.py: Handles the creation and movement of bullets.
  - alien.py: Defines the alien enemies and their behavior.
  - game_stats.py: Manages game statistics such as score and number of lives left.
  - button.py: Creates the play button and handles user interactions.
  - scoreboard.py: Displays the current score, level, and high score.
    
5. Game Mechanics
  - Initialization: Sets up the game environment, including the screen, game statistics, and game assets.
  - Event Handling: Responds to user inputs such as key presses and mouse clicks.
  - Gameplay Loop: Manages the game loop, including updating game objects, checking collisions, and redrawing the screen.
  - Collision Detection: Handles collisions between bullets and aliens, and between the ship and aliens.
  - Alien Fleet Management: Creates and updates the fleet of aliens, adjusts their movement direction, and handles their destruction.

Enjoy!
