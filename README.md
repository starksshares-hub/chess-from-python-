# ♟️ Chess From Python — The 7-Day No-AI Grind

> **Rule of the mission:**
> No sleeping on the bed.
> No going outside like a normal human.
> No AI writing the game for me.
>
> Until I build a working chess game in Python.
> Pure brain. Pure pain. Pure checkmate.

---
## 🚫 Challenge Rules — Ethical Learning Mode

This challenge is **No AI Code Mode**.

I am allowed to learn, understand, and research — but I am **not allowed to copy-paste my way to victory**.

### ✅ Allowed

* YouTube videos for **logic explanation only**
* Chrome / Google searches for concepts
* Official Python/module documentation
* Reading articles to understand ideas
* Watching documentaries or dev videos for motivation
* Debugging by thinking, testing, printing values, and reading errors
* Writing every line of project code myself

### ❌ Not Allowed

* No AI-generated code
* No AI fixing my code
* No AI writing functions, classes, or logic
* No copy-pasting code from YouTube
* No copy-pasting code from websites
* No downloading ready-made chess projects
* No pretending “I wrote it” after copying someone’s work

### 🧠 The Real Rule

I can use the internet to **learn the logic**.

But the final code must come from **my own brain, my own hands, and my own debugging pain**.

YouTube can explain how a rook moves.

Documentation can explain how Python works.

But the chess game must be built by me.

No shortcuts.

No fake skill.

No AI rescue mission.

Just learning, logic, mistakes, fixes, and checkmate.


## 🧠 What is this?

This is my **7-day challenge** to build a complete chess game using **Python**, without using AI to generate the code.

Yes, I know AI exists.
Yes, I know it could make this easier.
No, I am not using it for the actual build.

This project is my way of proving that I can sit down, suffer respectfully, debug like a warrior, and build something real from scratch.

---

## 🎯 Final Goal

By the end of 7 days, this project should become a playable chess game with:

* A proper chess board
* All chess pieces
* Legal moves
* Turn system
* Capturing
* Check detection
* Checkmate detection
* Clean Python code
* A simple but usable interface
* My sanity still loading...

---

## 🚫 Challenge Rules

1. **No AI-generated code**
2. I can search documentation and learn concepts
3. I can use Python docs, Stack Overflow, articles, and tutorials for understanding
4. I must write the actual code myself
5. I must commit progress daily
6. I cannot abandon the project just because a bishop started moving illegally
7. Bed access unlocks only after meaningful daily progress

---

## 🗓️ 7-Day Roadmap

### ✅ Day 1 — Setup + Board Creation

**Goal:** Create the base structure.

Tasks:

* Create project folder
* Set up Git and GitHub
* Create `main.py`
* Print an 8x8 chess board
* Represent board using lists
* Place pieces in starting positions
* Understand row/column coordinates

Expected output:

```text
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
```

Mental status:
Still confident. Dangerously confident.

---

### ✅ Day 2 — Move Input System

**Goal:** Make pieces move from one square to another.

Tasks:

* Take user input like `e2 e4`
* Convert chess notation into board indexes
* Move pieces on the board
* Stop moving empty squares
* Stop moving opponent pieces
* Add white/black turn system

Example:

```text
White move: e2 e4
Black move: e7 e5
```

Mental status:
Realizing chess coordinates are not as innocent as they look.

---

### ✅ Day 3 — Pawn, Rook, Bishop Logic

**Goal:** Add legal movement for basic pieces.

Tasks:

* Pawn movement
* Pawn first double move
* Pawn capture
* Rook straight-line movement
* Bishop diagonal movement
* Prevent jumping through pieces

Pain level:
Pawn logic will pretend to be easy. It is lying.

---

### ✅ Day 4 — Knight, Queen, King Logic

**Goal:** Finish legal movement for all pieces.

Tasks:

* Knight L-shaped movement
* Queen movement
* King one-square movement
* Prevent illegal moves
* Improve error messages

Expected errors:

```text
Invalid move.
That piece cannot move there.
Bro, that is not how a knight works.
```

Mental status:
The knight is either genius or completely unhinged.

---

### ✅ Day 5 — Check Detection

**Goal:** Detect when a king is under attack.

Tasks:

* Find king position
* Check if enemy piece attacks king
* Prevent moves that leave own king in check
* Display warning when check happens

Example:

```text
White king is in CHECK!
```

Mental status:
Now the board has trust issues.

---

### ✅ Day 6 — Checkmate + Game Ending

**Goal:** Make the game actually end properly.

Tasks:

* Detect if king is in check
* Test all possible legal moves
* If no legal move saves king, declare checkmate
* Add stalemate if possible
* Add winner message

Example:

```text
CHECKMATE.
Black wins.
White king has left the server.
```

Mental status:
The game is now smarter than Day 1 me.

---

### ✅ Day 7 — Polish + README + Final Demo

**Goal:** Make it presentable.

Tasks:

* Clean code
* Split logic into files if needed
* Add comments
* Add screenshots or terminal demo
* Update README
* Push final version to GitHub
* Record short demo if possible

Final mood:

```text
7 days ago: I can build chess easily.
Today: I respect every game developer alive.
```

---

## 🧩 Planned File Structure

```text
chess-from-python-/
│
├── main.py
├── board.py
├── pieces.py
├── moves.py
├── game.py
├── README.md
└── screenshots/
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Version Control:** Git + GitHub
* **Interface:** Terminal first
* **Possible upgrade later:** Pygame GUI

---

## 🚀 Future Upgrade Ideas

After the basic version works, I may add:

* Pygame graphical board
* Drag-and-drop pieces
* Move history
* Timer
* Restart option
* Save/load game
* Basic chess bot
* Sound effects
* “Bro that move is illegal” mode

---

## 📌 Daily Progress Log

### Day 1

Started the challenge.
Mission accepted.
Bed access currently locked.

Progress:

* [x] Project created
* [x] Git initialized
* [x] Board printed
* [x] Pieces placed
* [x] First commit pushed

---

### Day 2

Coming soon...

---

### Day 3

Coming soon...

---

### Day 4

Coming soon...

---

### Day 5

Coming soon...

---

### Day 6

Coming soon...

---

### Day 7

Coming soon...

---

## 🧠 Why I Am Doing This

Because watching tutorials forever is not learning.

Because copying code is not building skill.

Because I want to become the type of developer who can think, break problems down, debug, and actually finish projects.

This chess game is not just a game.

It is a discipline test.

A logic test.

A patience test.

And possibly a sleep deprivation documentary.

---

## 🏁 Final Declaration

I will build this chess game in 7 days.

No AI-generated code.

No excuses.

No bed until progress.

No outside world until the king falls.

**Checkmate or collapse.**
