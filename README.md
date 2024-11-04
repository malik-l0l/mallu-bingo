
<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Mallu-Bingo

## Description
Sometimes, classes can feel a bit dull, and that’s when I turn to my favorite paper games! One game I absolutely love is "Bingo." It's a simple yet strategic paper game that brings a spark of excitement to the day. Whether I'm playing with friends or competing to see who can get to that magical "Bingo!" first, it always adds a fun twist to the usual routine.

In the old days, every kid's notebook had a special space dedicated to playing Bingo, making it a beloved pastime that brightened our school days. Those moments of friendly competition and laughter created memories that still make me smile! This game is especially popular among the "Useless Backbench Team," who always find a way to turn the most boring classes into a lively competition.


## Game Instructions

Bingo is a 2 player game which has so many versions. The instructions for this version are given below:

1. Create a board with 5 rows and 5 columns which have numbers from 1-25 placed randomly.  
   **Note:** Each player must hide their board throughout the game until finish. Player 1's board may or may not be the same as player 2's board.

2. Player 1 will tell a number which is not marked in the board, then both players mark that number in their board.

3. Then, Player 2 will tell a number which is not marked in the board, then both players mark that number in their board.

4. Repeat steps 2 and 3 until someone wins.

5. If every number in a row, column, or diagonal is marked, the player gets a point which is represented as 'B I N G O'.  
   **Example:** Given board:
   ```python
   [
       ["█", "█", "█", "█", "█"],
       [13, 15, 20, "█", "█"],
       [11, 12, "█", 14, "█"],
       [16, "█", 18, 19, "█"],
       ["█", 22, 23, 24, "█"],
   ]
   Here, the player with this board gets 3 points (1 row, 1 column, 1 diagonal), which is represented as 'B I N'.

6. `"Whoever gets 5 points AKA 'B I N G O' first WINS!"`

## Game Overview

In this 2-player game, players will take turns calling out numbers and marking them on their boards. The objective? Be the first to mark five numbers in a row, column, or diagonal to achieve 'B I N G O'! The fun doesn’t stop there; with our unique game modes, you can choose how challenging you want your experience to be.

## Game Modes

### 🎮 Easy Mode
In Easy Mode, you can relax and enjoy the game without breaking a sweat! `The computer is completely Useless here`, making it easy for players to win. Perfect for beginners or anyone looking for a casual game experience!

### 🎮 Medium Mode
Step it up with Medium Mode! Here, the competition heats up as the computer employs a clever algorithm designed to mimic human strategies. It will analyze the board and make decisions based on the data, providing a balanced challenge. `Here both Player or Computer can be Useless`, both players still have an equal chance of winning, so bring your best game face!

### 🎮 Hard Mode
Are you ready for a true challenge? In Hard Mode, the computer is a formidable opponent that will always win. No matter how skilled you think you are, `prepare to feel utterly Useless as you face this relentless competitor!` This mode is perfect for those who want to push their limits and experience the thrill of near-impossible odds. Only the bravest players dare to take on this mode!






## Technical Details

| Versions       | Description                                          | Access Link                        |
|----------------|------------------------------------------------------|------------------------------------|
| Script Version  | Can be played through terminal just by executing the project. | [Click here to access code]([#](https://github.com/malik-l0l/mallu-bingo/tree/main/%23script-only))   |
| Web Version     | Play the game through a website.                     | [Click here to access code]([#](https://github.com/malik-l0l/mallu-bingo)s)                    |


### Technologies/Components Used
For Software:
- For Scripts we used Python only wth random library
- For web version we used Python Flask




# Run - script version
1. Clone the repo
```
git clone https://github.com/malik-l0l/mallu-bingo.git
```
2. Navigate into the script-only folder in project directory
```
cd mallu-bingo
```
3. Run the Python script
```
python mallu-bingo.py

```


# Run - web version
#### Installation


1. clone the repository
```
git clone https://github.com/malik-l0l/mallu-bingo.git
```

2. navigate to the directory
```
cd bingo-game
```

3. (optional) create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate` or .\.venv\Scripts/activate
```
4. install requirements if needed
```
pip install -r requirements.txt
```
5. Run

```
python app.py
```




# Screenshots (Add at least 3)

1. The Global Variables : 
![Screenshot (164)](https://github.com/user-attachments/assets/8f6ffcb3-c4c6-473d-94fa-c0888d62536c)
Customize your game experience by adjusting the following settings within the code:

| Setting               | Description                                                                                                                                               | Example Values       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| `REMOVED_NUMBER`      | Defines the symbol used to mark numbers that have been selected. You can choose any symbol to represent marked numbers on the board.                        | `"█"`, `"֍"`, `"•"`, `"Ø"` |
| `SHOW_COMPUTER_BOARD` | Set this to `True` to display the computer's board during the game, allowing players to observe its strategy. If `False`, the computer’s board remains hidden. | `True`, `False`      |
| `CHALLENGE`           | Determines the difficulty level of the game, influencing the computer's strategy: <br> - **`easy`**: The computer plays weakly, making it easy for the player to win. <br> - **`medium`**: The computer uses a balanced strategy that mimics human decision-making. <br> - **`hard`**: The computer plays optimally, making it nearly impossible for the player to win. | `"easy"`, `"medium"`, `"hard"` |


![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*



### Project Demo
# Video

https://github.com/user-attachments/assets/abe3047d-e904-45f1-a7e7-5a9ad5457a2b
playing the game in script version.


## Details

| Team | Name | College |
|---|---|---|
| Individual | Saleem Malik | GEC Kozhikode |
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
