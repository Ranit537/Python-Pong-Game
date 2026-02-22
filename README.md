# 🏓 Python Pong Game

A classic **2-Player Pong Game** built using Python’s Turtle graphics module. Control paddles, bounce the ball, score points, and compete with a friend in real-time.

---

## 🎮 Features

* 🏓 Two-player gameplay
* ⚡ Smooth ball physics
* 🎯 Collision detection (walls + paddles)
* 📊 Live scoreboard
* 🎮 Keyboard controls for both players
* 🖥 Real-time rendering

---

## 📦 Requirements

No external libraries required ✅
Uses only built-in Python modules:

* turtle
* time

Check Python installation:

```
python --version
```

---

## ▶️ How to Run

Clone repository:

```
git clone https://github.com/Ranit537/Python-Pong-Game.git
cd Python-Pong-Game/PongGame
```

Run the game:

```
python main.py
```

---

## 🎮 Controls

### Left Player

| Key | Action    |
| --- | --------- |
| W   | Move Up   |
| S   | Move Down |

### Right Player

| Key | Action    |
| --- | --------- |
| P   | Move Up   |
| L   | Move Down |

---

## 📁 Project Structure

```
Python-Pong-Game/
│
├── PongGame/
│   ├── main.py
│   ├── paddle.py
│   ├── ball.py
│   └── scoreboard.py
│
├── README.md
└── .gitattributes
```

---

## 🧠 How Game Works

Game logic loop:

1. Create screen
2. Create paddles
3. Create ball
4. Listen for player input
5. Move ball continuously
6. Detect paddle collisions
7. Detect wall collisions
8. Update score when ball passes paddle
9. Reset ball position

---

## 🛠 Troubleshooting

**Game window not opening**

* Ensure Python is installed correctly

**Controls not working**

* Click inside game window first

**Module not found**

* Run file from inside `PongGame` folder

---

## 📜 License

This project is open source and free to use.

---

## 👨‍💻 Author

**Ranit537**
GitHub: https://github.com/Ranit537

---

⭐ Star this repo if you enjoyed the game!
