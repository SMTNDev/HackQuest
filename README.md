# HackQuest 🕵️‍♂️💻

[![Version](https://img.shields.io/badge/version-1.6-brightgreen?style=for-the-badge&logo=semantic-release)](https://github.com/SMTNDev/HackQuest) [![📜 License](https://img.shields.io/badge/License-Apache-blue?style=for-the-badge&logo=bookstack)](https://github.com/SMTNDev/HackQuest)  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/) [![Platform](https://img.shields.io/badge/Platform-Termux-lightgrey?style=for-the-badge&logo=android&logoColor=white)](https://termux.dev/) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?style=for-the-badge&logo=github)](#) [![PyPI](https://img.shields.io/pypi/v/HackQuest?style=for-the-badge&color=orange&logo=pypi)](https://pypi.org/project/HackQuest/) [![Contributions](https://img.shields.io/badge/contributions-welcome-orange?style=for-the-badge&logo=git)](#contributing)

![HackQuest Logo](https://i.ibb.co/QCFhw20/Rich-burgundy-and-deep-blue-modern-flat-design-style-Hack-Quest-logo-simple-two-dimensional-shapes-s.jpg)

**HackQuest** is a terminal-based hacking simulator game designed to test your problem-solving and ethical hacking skills. Solve challenges, crack codes, and advance through increasingly difficult levels in this immersive, text-based environment.

---

## 🎮 Features

- 🚀 **Dynamic Welcome Screen**: Animated ASCII art, hacker-themed quotes, and polished prompts.
- 🖼️ **Advanced UI Elements**: Rich separators, typewriter effects, and dynamic text animations.
- 🔓 **Multiple Levels**:
  - **Level 1**: Password Retrieval.
  - **Level 2**: File Decryption.
  - **Level 3**: Log Analysis.
- 🎲 **Mini-Game**: Integrated 2048 terminal game for fun breaks.
- 🔐 **Encryption Challenges**: Test your cryptography skills.
- 🌟 **Dynamic Commands**: Simulated hacking tools like `scan`, `decrypt`, and more.

---

## 📸 Screenshots

### **Welcome Screen**
![Welcome Screen](https://i.ibb.co/NCFpfFm/Screenshot-20250111-163949.jpg)

### **Interactive Commands**
![Interactive Commands](https://i.ibb.co/9v3YtGG/IMG-20250111-014838.jpg)

### **Level Challenges**
![Level Challenges](https://github.com/user-attachments/assets/b79bdedb-2dc6-43d1-af5f-0e393af64951)

---

## 📋 Requirements

- **Python 3.8+**
- Unix/Linux or Windows (with `windows-curses`)
- Rust installed (if using Rust integration features)

### Python Dependencies

All dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/SMTNDev/HackQuest.git
    cd HackQuest
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the game**:

    ```bash
    python3 src/main.py
    ```

4. **For Windows users**:  
   Install `windows-curses`:

   ```bash
   pip install windows-curses
   ```
5. **Install HackQuest directly from PyPI**:
   ```bash
   pip install HackQuest
   ```
6. **Run the game**:
   ```bash
   hackquest
   ```

---

## 🎯 How to Play

1. Launch the game:
   ```bash
   python3 src/main.py
   ```

2. Use the following commands to navigate the game:
   - `help` - View all available commands.
   - `level1`, `level2`, `level3` - Start levels.
   - `scan`, `decrypt` - Simulate hacking tools.
   - `exit` - Quit the game.

3. Complete levels by solving challenges and advancing to the next!

---

## ✨ HackQuest Commands

| Command     | Description                         |
|-------------|-------------------------------------|
| `help`      | Show the help menu                 |
| `level1`    | Start Level 1 (Password Retrieval) |
| `level2`    | Start Level 2 (File Decryption)    |
| `level3`    | Start Level 3 (Log Analysis)       |
| `scan`      | Simulate a scanning tool           |
| `decrypt`   | Simulate decryption process        |
| `exit`      | Exit the game                      |

---

## 🛠️ Contribution

Contributions are welcome! If you'd like to improve the game, follow these steps:

1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## ❤️ Support

If you like the project, please consider supporting:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/SMTNDev)

---

## 📝 License

This project is licensed under the [Apache-2.0 License](https://github.com/SMTNDev/HackQuest#).

---

## 🌟 Acknowledgments

- Inspired by the spirit of ethical hacking and problem-solving.
- Thanks to all contributors and supporters of open-source projects!
