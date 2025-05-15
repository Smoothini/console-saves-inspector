# 🎮 Console Saves Inspector

A lightweight tool to inspect console save game folders and display the names of the games based on their Title IDs!

Yet another [Flet](https://flet.dev/) project for a simple and clean desktop UI. Built because I backed up my ps3 saves, and apparently I had close to 300, which made it a bit hard to find specific ones. Initially made for the Playstation 3, now expanded!

**All Title IDs and game names are used for identification purposes only. This project is not affiliated with or endorsed by Sony Interactive Entertainment.**

**WORK IN PROGRESS, WORKS BUT NEEDS DROPDOWN TO SELECT CONSOLE, ELSE HAVE TO DO MANUALLY IN CODE**

---

## ✨ Features

- ✅ Select a folder containing save games
- 🔍 Automatically display game titles
- ⚡️ Fast, minimal interface (no internet required)
- 🌍 Displays the game region
- 📼 Displays also the game medium, albeit for some reason this is a hit or miss
- 🆎 Clicking on any of the table headers will order the entries alphabetically based on that column

_NOTE: I've only tested on windows for now, but feel free to open an issue or make a merge request if changes are needed for other platforms!_

---

## 💽 Supported Consoles as of now

- Playstation 3
- Playstation Vita

## 📸 Screenshot

![Screenshot](screenshot.png)
  - For some reason, my savegame for the Japanese copy of Puppeteer appears as Buzz Junior Dinomania. Somehow they have the same title ID.

---

## 🚀 Getting Started

### Option 1: Run from Source

1. Clone the repo:
  ```bash
  git clone https://github.com/smoothini/ps3-saves-inspector.git
  cd ps3-saves-inspector
  ```
2. Install dependencies
  ```bash
  pip install flet
  ```
3. Run the app, while making sure the `datafiles` folder  is in the same location as the `app.py`
  ```bash
  python app.py
  ```
4. Select a console
5. Select a folder where you have multiple save games for that console
6. ✨ Enjoy! ✨

### Option 2: Standalone Executable
  - Coming soon

## 🙋‍♂️ Contributing
Pull requests and suggestions are welcome!
If you'd like to add more Title IDs or improve the UI, feel free to fork and submit a PR, frontend ain't really my thing.

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it, even in commercial applications — just include the original license.

© 2025 Smoothini