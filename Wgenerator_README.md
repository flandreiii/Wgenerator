<div align="center">

```
██╗    ██╗ ██████╗ ███████╗███╗   ██╗
██║    ██║██╔════╝ ██╔════╝████╗  ██║
██║ █╗ ██║██║  ███╗█████╗  ██╔██╗ ██║
██║███╗██║██║   ██║██╔══╝  ██║╚██╗██║
╚███╔███╔╝╚██████╔╝███████╗██║ ╚████║
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝

 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

**A fast wordlist and password generator for Termux and Linux**  
*Python · Terminal · Termux · Security Research*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Author](https://img.shields.io/badge/Author-flandreiii-cyan?style=flat-square)
![Type](https://img.shields.io/badge/Type-Wordlist%20Generator-orange?style=flat-square)

</div>

---

## 📋 What is Wgenerator?

**Wgenerator** is a fast and flexible wordlist generator built in Python, fully compatible with **Termux** on Android. It generates custom word combinations that can be used for security testing, CTF challenges, or password auditing on systems you own.

Give it a set of rules, and it outputs a ready-to-use wordlist straight to your terminal or to a file.

---

## ✨ Features

- 📝 **Custom wordlist generation** — define your own patterns and rules
- ⚡ **Fast output** — generates large lists quickly
- 📱 **Termux compatible** — runs natively on Android
- 🖥️ **Cross-platform** — works on Linux, macOS and Windows too
- 💾 **Save to file** — export your wordlist for later use
- 🐍 **Pure Python** — no heavy dependencies, easy to modify

---

## 📋 Requirements

| Requirement | Details |
|---|---|
| **Python** | 3.x |
| **App** | [Termux](https://f-droid.org/packages/com.termux/) from F-Droid (Android only) |

> ⚠️ **Install Termux from F-Droid**, not the Play Store. The Play Store version is outdated and may cause issues.

---

## 🚀 Installation

### Termux (Android)

```bash
# Step 1 — Update packages and install dependencies
pkg update && pkg upgrade
pkg install python git

# Step 2 — Clone the repo
git clone https://github.com/flandreiii/Wgenerator.git
cd Wgenerator

# Step 3 — Run it
python wgenerator.py
```

### Linux

```bash
# Step 1 — Install Python and Git
sudo apt install python3 git      # Debian / Ubuntu
# or
sudo pacman -S python git         # Arch Linux

# Step 2 — Clone the repo
git clone https://github.com/flandreiii/Wgenerator.git
cd Wgenerator

# Step 3 — Run it
python3 wgenerator.py
```

### Windows

```bash
# Step 1 — Install Python from https://python.org
#           Install Git from https://git-scm.com

# Step 2 — Clone the repo
git clone https://github.com/flandreiii/Wgenerator.git
cd Wgenerator

# Step 3 — Run it
python wgenerator.py
```

---

## 🛠️ Usage

```bash
python wgenerator.py
```

Follow the on-screen prompts to configure your wordlist — set character sets, lengths, patterns, and output destination.

---

## 💡 What is a Wordlist?

A **wordlist** is a file containing a large list of words, passwords, or character combinations. They are commonly used in:

- 🔐 **Password auditing** — testing the strength of passwords on your own systems
- 🏁 **CTF challenges** — Capture The Flag competitions
- 🔍 **Security research** — testing login forms and authentication systems you own
- 🧪 **Fuzzing** — generating test inputs for your own applications

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` | Run `pkg install python` in Termux, or `sudo apt install python3` on Linux |
| `git: command not found` | Run `pkg install git` in Termux |
| Output file not created | Make sure you have write permissions in the current directory |
| Termux crashes | Reinstall from **F-Droid**, not the Play Store |
| Script runs slowly on large lists | This is normal for very large character sets — reduce the length or character range |

---

## 📁 Project Structure

```
Wgenerator/
├── wgenerator.py    # Main generator script
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

---

## 🤝 Contributing

Contributions are always welcome!  
Feel free to open an issue or submit a pull request.

Ideas for future features:
- [ ] Rule-based mutations (leet speak, capitalization, etc.)
- [ ] Import a base wordlist and mutate it
- [ ] Combine multiple wordlists
- [ ] Progress bar for large generations
- [ ] Filter by length or pattern
- [ ] Output directly to a `.txt` file

---

## ⚠️ Disclaimer

Wgenerator is intended for **educational purposes** and for use on systems, accounts, and applications that you own or have explicit permission to test. Using this tool against systems without authorization is illegal. The author is not responsible for any misuse.

---

## 📜 License

```
MIT License

Copyright (c) 2026 flandreiii

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

**Made by [flandreiii](https://github.com/flandreiii)**

*Wgenerator — build your wordlist, own your security 🔐*

</div>
