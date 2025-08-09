# 🚀 Starship vs Asteroids

A small **Pygame** project where a triangular starship can move around and shoot at asteroids (represented as circles).  
Currently, it’s a simple game prototype — but there’s plenty of room for upgrades.

---

## 🎮 How to Play

- **Move the ship** — Arrow keys or WASD (depending on your control setup)
- **Shoot asteroids** — Spacebar
- Avoid collisions with asteroids

---

## 📦 Requirements

- Python 3.12
- [uv](https://github.com/astral-sh/uv) (for running and dependency management)

Install `uv` (if you don't have it yet):

```bash
pip install uv
```

---

## ▶️ Install & Run the Game

Install dependencies:

```bash
uv pip install pygame
```

Run the game:

```bash
uv run main.py
```

---

## ✨ Current Features

- Player-controlled triangular starship
- Asteroids represented as moving circles
- Basic shooting mechanic
- Simple collision detection
- Objects disappear when they collide

---

## 🔮 Possible Future Improvements

This is currently a small project, but potential features include:

1. **Optimize collision logic** to avoid unnecessary calculations  
2. **Refactor code** for better readability and maintainability  
3. **Add a scoring system** so players can compete with themselves or friends  
4. **Implement multiple lives** and respawning after destruction  
5. **Add asteroid explosion effects** for visual feedback  
6. **Add acceleration** to player movement for smoother control  
7. **Screen wrap-around** so objects reappear on the opposite side instead of disappearing  
8. **Add a background image** for a more engaging look  
9. **Different weapon types** for more variety in gameplay  
10. **Lumpy asteroid shapes** instead of perfect circles  
11. **Triangular hitbox** for the ship to improve collision accuracy  
12. **Shield power-up** to temporarily protect the player  
13. **Speed power-up** for temporary movement boost  
14. **Bombs** that can be dropped for area damage  

---

## 🛠️ Notes

This is an experimental learning project for Pygame.  
The focus is on keeping the game simple while building a foundation for possible expansion.

---
