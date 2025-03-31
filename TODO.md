# 📝 Cloud Based — TODO List

A roadmap to building a dystopian text-based afterlife simulator.

---

## ✅ MVP Tasks (Minimum Viable Product)

### **Core Gameplay**

- [x] Create player stats: Storage, Memory Integrity, Subscription Days, SoulCredits
- [x] Display player stats each day
- [x] Add random daily event system
- [x] Implement at least 3 unique events
  - [x] Memory corruption event
  - [x] Relative cancels subscription
  - [x] CloudCorp ad offer
- [x] Allow player choices that affect stats
- [x] Add win/lose conditions:
  - [x] Subscription Days = 0 → Game Over
  - [x] Memory Integrity ≤ 0 → Game Over
- [x] Create main game loop

### **Polish**

- [x] Add simple console text flavor and humor
- [ ] Write README.md
- [ ] Write TODO.md (you’re here!)

---

## 🚀 Roadmap Tasks (Post-MVP)

### Phase 1 — Structure & Clean-Up

- [ ] Split `main.py` into separate files:
  - [ ] `player.py` → Player stats & methods
  - [ ] `events.py` → Event system
  - [ ] `game_loop.py` → Core loop
  - [ ] `utils.py` → Display functions
- [ ] Add save/load system (optional)

---

### Phase 2 — Content Expansion

- [ ] Write at least 10 unique daily events
- [ ] Add branching story arcs:
  - [ ] Family Fund Arc
  - [ ] CloudCorp Compliance Arc
  - [ ] Hacker Collective Arc
  - [ ] Identity Crisis Arc
  - [ ] Eternal Subscription Arc
- [ ] Create at least 3 distinct endings

---

### Phase 3 — Replayability & UX

- [ ] Add difficulty settings
- [ ] Add random glitch events
- [ ] Track stats and choices for replay summary
- [ ] Polish text & user input handling

---

### Phase 4 — Advanced Features (Optional)

- [ ] Refactor into object-oriented structure (classes)
- [ ] Move event data to `.json` or `.txt` files
- [ ] Add menu system (New Game, Load Game, Exit)
- [ ] Add color output to console (using `colorama`)

---

### Phase 5 — Stretch Goals

- [ ] Build GUI version (Tkinter or PySimpleGUI)
- [ ] Convert to web app (Flask or Django)
- [ ] Add sound effects and music
- [ ] Package and release a playable version

---

## 🌟 Long-Term Goal

Use the skills and structure learned here to build:

- Language learning apps
- Vocabulary analysis tools
- Interactive learning games

**Your dystopian death simulator is secretly coding practice for your future projects.**
