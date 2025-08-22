# 🐷🎲 PIG Dice Roll Game (Python)

A fun and beginner-friendly **multi-player dice game** based on the classic *Pig* game - implemented entirely in Python and run from the terminal.

---

## 📖 How to Play

- Each player takes turns rolling a **6-sided die**.
- On their turn:
  - If they roll a **1** → their turn ends with **0 points** for the round.
  - If they roll **2–6** → it's added to their *current round score*.
- The player can choose to **"Hold"** at any time:
  - Their round score gets added to their total score.
  - The turn passes to the next player.
- First to reach or exceed the **target score** wins!

---

## ✨ Features

- 🎮 Supports **2 to 4 players**
- 🥇 Customizable **target score** (e.g., 20, 50, 100)
- 💬 Friendly prompts and clear feedback
- ✅ Input validation (player count, command options)
- 🐍 Simple Python code - great for learning control flow and game loops

---

## ⚙️ Requirements

- Python 3.x
- No external libraries required (uses `random` and `input()`)

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed
2. Run the script:

    ```bash
    python pig_dice_game.py
Follow the prompts in your terminal!

---

## 🖥️ Sample Gameplay

```
Welcome to the PIG Dice Roll Game.🐷🎲
Choose a target score (like 20, 50, 100): 20
Enter the number of players (2-4): 2

Player number 1 turn has just started.
Your total score is:  0

Roll or Hold: roll
🎲 Dice Roll: 5
Your Score is:  5
Roll or Hold: hold
You held at 5 points. Your total score is now 5
...

🎉 Congratulations Player 2, you won with 21 points! 🎉
```

---

## 🎯 What I Learned

- Using random.randint() for dice simulation
- while and for loops for turn-based logic
- Managing state across multiple players
- Handling and validating user input

---

## 👨‍💻 Made By

Crafted with 🐍 by [Toshaksha](https://github.com/Toshaksha)
