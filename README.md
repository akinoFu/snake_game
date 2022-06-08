# Snake Game
This is a snake game developed by [@shaniahn](https://github.com/shaniahn), [@akinoFu](https://github.com/akinoFu) and [@jacev58](https://github.com/jacev58) using **Python** with **Pygame** and **Flask** as a school project in Computer Information Technology program at British Columbia Institute of Technology.
When the game begins, the snake moves around the surface. The player controls the snake with the arrow keys and crashes it into apples to score points. The more points earned, the longer the snake becomes. Player needs to control the snake not to hit the wall.

## Compornents
This application has three parts: game, api, and test
### game
- Allow users play the game
- All the interface is developed using **Pygame**
- The code is organized by **Model-view-controller (MVC)** patterns
### api
- Allow the game to record and show scores via the APIs
- Developed using **Flask**
### test
- Test the source code for the "game" part using **Pytest**

## How to Run
1. Clone the repo to local
2. Install Pygame
3. Run *game/run.py* and *api/run.py*
4. The game starts and the score board will be accessible with http://127.0.0.1:5000/
