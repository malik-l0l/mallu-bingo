
<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# 🎲 Mallu-Bingo
You can start playing right away with one of these options:

- Play Online: [mallu-bingo](https://mallu-bingo.vercel.app)
- Play in Terminal: Follow the instructions below to get started with the script version
---

## 📝 Description
Ever feel like classes drag on forever? That’s when my favorite paper game, **Bingo**, comes to the rescue! This classic game of strategy and chance was a staple in every kid's notebook, bringing life to even the dullest school days. Whether it's competing with friends or racing to that magical “Bingo!” moment, it’s a surefire way to add fun to any routine.

Back in the day, Bingo was a beloved pastime of the “Useless Backbench Team,” always ready to turn any boring class into a lively competition. Now, you can relive those memories with *Mallu-Bingo*, a game that brings back the thrill of friendly competition!

---
## 💬 Game Instructions

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

## 🗺️ Game Overview

In this 2-player game, players will take turns calling out numbers and marking them on their boards. The objective? Be the first to mark five numbers in a row, column, or diagonal to achieve 'B I N G O'! The fun doesn’t stop there; with our unique game modes, you can choose how challenging you want your experience to be.

### 🌟 Game Modes

### 🟢 Easy Mode
In Easy Mode, you can relax and enjoy the game without breaking a sweat! `The computer is completely Useless here`, making it easy for players to win. Perfect for beginners or anyone looking for a casual game experience!

### 🟡 Medium Mode
Step it up with Medium Mode! Here, the competition heats up as the computer employs a clever algorithm designed to mimic human strategies. It will analyze the board and make decisions based on the data, providing a balanced challenge. `Here both Player or Computer can be Useless`, both players still have an equal chance of winning, so bring your best game face!

### 🔴 Hard Mode
Are you ready for a true challenge? In Hard Mode, the computer is a formidable opponent that will always win. No matter how skilled you think you are, `prepare to feel utterly Useless as you face this relentless competitor!` This mode is perfect for those who want to push their limits and experience the thrill of near-impossible odds. Only the bravest players dare to take on this mode!






## 🛠️ Technical Details

| Versions       | Description                                          | Access Link                        |
|----------------|------------------------------------------------------|------------------------------------|
| Script Version  | Play the game in the terminal | [Click here to access code](https://github.com/malik-l0l/mallu-bingo/tree/main/%23script-only)   |
| Web Version     | Play the game on a web interface.                     | [Click here to access code](https://github.com/malik-l0l/mallu-bingo)                   |



## 🧩 Technologies Used
For Software:

- Script Version: Python with the random library.
- Web Version: Python (Flask), hosted on Vercel.


### 🏃 Run - script version
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


### 🏃 Run - web version
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




## 📸 Screenshots 

1. Script Version Settings :  
![Screenshot (164)](https://github.com/user-attachments/assets/8f6ffcb3-c4c6-473d-94fa-c0888d62536c)
Customize your game experience by adjusting the following settings within the code:

| Setting               | Description                                                                                                                                               | Example Values       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| `REMOVED_NUMBER`      | Defines the symbol used to mark numbers that have been selected. You can choose any symbol to represent marked numbers on the board.                        | `"█"`, `"֍"`, `"•"`, `"Ø"` |
| `SHOW_COMPUTER_BOARD` | Set this to `True` to display the computer's board during the game, allowing players to observe its strategy. If `False`, the computer’s board remains hidden. | `True`, `False`      |
| `CHALLENGE`           | Determines the difficulty level of the game, influencing the computer's strategy: <br> - **`easy`**: The computer plays weakly, making it easy for the player to win. <br> - **`medium`**: The computer uses a balanced strategy that mimics human decision-making. <br> - **`hard`**: The computer plays optimally, making it nearly impossible for the player to win. | `"easy"`, `"medium"`, `"hard"` |

2. Web Version Landing Page
![Screenshot (165)](https://github.com/user-attachments/assets/1ccc4243-ef30-4cc7-9c17-c1bbf58f9e4d)
The landing page provides instructions and an option to show the computer’s board during gameplay.

3. Bingo board during game-play
![Screenshot (168)](https://github.com/user-attachments/assets/ecbeac9d-da81-4923-ba7a-1a57df3faaf4)
Experience the thrill of marking numbers and achieving BINGO.

4. Victory Screen
![Screenshot (167)](https://github.com/user-attachments/assets/8d458dec-3643-4dbf-8913-9209b979ddfd)
The win condition is to get all "B I N G O" letters,so achieve victory by getting all letters in B I N G O before your opponent! Here the player won because he got all BINGO letters before the computer.

## 🎥 Video

1. Game play walk through [script version]

   
https://github.com/user-attachments/assets/abe3047d-e904-45f1-a7e7-5a9ad5457a2b


playing the game in script version in terminal.


2.Game play walk through [web version]


https://github.com/user-attachments/assets/58b5158d-f64f-4ce3-b52f-e888541606bb


playing the game in web version in browser.





## 👥 Me ??...

| Team | Name | College |
|------|------|---------|
| Individual | Saleem Malik | GEC Kozhikode |
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
