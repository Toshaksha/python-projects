# 🔤 Word Guessing Game

Welcome to the **Word Guessing Game**!
Test your vocabulary and deduction skills by guessing hidden words based on the difficulty level you choose.

---

## 🎮 How to Play

1. Select a difficulty level:
   - `Easy`
   - `Medium`
   - `Hard`

2. You will be told how many letters are in the word.

3. Start guessing one letter at a time:
   - Correct letters will be revealed in their positions.
   - Incorrect guesses will be tracked.

4. Keep guessing until you complete the word, or type `'q'` to quit.

---

## 🧠 Features

- Three difficulty levels with different word pools.
- Shows number of letters in the mystery word.
- Tracks number of guesses.
- Provides feedback on valid/invalid inputs.
- Handles repeated letters and case insensitivity.
 
---

## 🛠️ Requirements

- Python 3.x

---

## 🚀 How to Run

1. Clone or download the repository  
2. Run the script using Python 3:  
   ```bash
   python word_guess.py
3. Follow the on-screen prompts to play

---

## 📌 Sample Output
```
Welcome aboard.
Ready to solve the mysteries!!
Rules:
- You will be given a word to guess based on the difficulty you choose.
- You will be told how many letters are there in the word.
- After every guess, you'll be told whether you made a correct guess or not.
- Keep guessing until you guess the word correctly.
- Type 'q' at any time to quit the game.

What level you wanna play: Easy, Medium or Hard
> easy
Number of letters in the word is:  3
Current guess: ___
Enter a letter (or 'q' to quit): a
Good guess!
Current guess: _a_
Enter a letter (or 'q' to quit): t
Wrong guess!
Current guess: _a_
Enter a letter (or 'q' to quit): c
Good guess!
Current guess: ca_
Enter a letter (or 'q' to quit): t
Good guess!
Congratulations!!! You guessed the word correctly in 4 guesses.
```
---

## 🎯 What I Learned

- Using functions to structure code
- Handling user input validation
- Working with string manipulation and lists
- Implementing game logic with loops and conditionals
- Using random choices for word selection

---

## 🙌 Credits
📚 Made by Toshaksha, powered by Python — and occasionally saved by lucky guesses 😅.