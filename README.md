
# Basic Keyboard Event Logger (Theory & Educational Purpose)

A safe, transparent, consent-based keyboard event logger built for **theory demonstrations**, **HCI studies**, and **introductory cybersecurity coursework**.  
This program does **not** hook into the operating system, does **not** monitor other applications, and does **not** run in the background.  
All keystrokes are captured **only inside the program’s visible text box**, with the user’s full awareness.

---

## ✅ Purpose

This project demonstrates:

- Event-driven keyboard capture in Python  
- Basic logging with timestamps  
- GUI-driven input using Tkinter  
- Safe and ethical approaches to input logging  
- How keystroke events can be serialized for analysis  

It is suitable for:

- College practicals  
- Theory viva  
- Intro-level cybersecurity reports  
- HCI or usability data collection  
- Demonstrating logging structures without touching sensitive system APIs

---

## ⚠️ Ethical & Legal Notice

This tool is designed **only** for:

- Educational explanation  
- Controlled lab environments  
- Explicit user-consent scenarios  

It **cannot** and **must not** be used to monitor other apps, background input, or any user without permission.  
This is **not a keylogger** in the malicious sense.

---

## 🔧 Features

### Core Features
- Captures keyboard events **only inside its own window**
- Visible Tkinter GUI with user text box
- Timestamps for each key press
- Logs saved to a simple text file (`basic_keylog.txt`)
- Human-readable log format

### Technical Highlights
- Uses Python 3’s `tkinter` for GUI
- Uses `dataclasses` for clear event modeling
- Uses `pathlib` for cross-platform file paths
- Clean and minimal design (under 100 lines)

---

## 📦 Requirements

- Python **3.8 or higher**
- No external dependencies  
  (`tkinter` ships with Python)

---

## 🚀 Quick Start

```bash
python basic_keylogger.py
```

A window will open with a text box.  
Type inside it. All keys typed in that text box will be logged.

---

## 📁 Log Output Example

```
[2025-01-12 14:20:55] H
[2025-01-12 14:20:56] e
[2025-01-12 14:20:56] l
[2025-01-12 14:20:56] l
[2025-01-12 14:20:57] o
[2025-01-12 14:20:57] [BackSpace]
```

Logs are saved in:

```
basic_keylog.txt
```

Each entry contains:

- Timestamp  
- Key pressed  

---

## 🧠 Internal Architecture

### 1. `KeyEvent`
Represents a single keystroke with timestamp and value.

### 2. `LogManager`
Handles file writing and event serialization.

### 3. `BasicKeyLoggerApp`
Main GUI application using Tkinter.  
Captures `<Key>` events only inside its own widget.

### Event Flow
```
Tkinter Key Event
        ↓
on_key_press()
        ↓
KeyEvent dataclass
        ↓
LogManager.write_event()
        ↓
basic_keylog.txt
```

---

## 🧪 Educational Use Cases

### For Cybersecurity Students
- Demonstrates ethical input logging  
- Contrasts harmless event capture vs system-wide keylogging  
- Helps explain the difference between GUI-bound logging and OS hooks  

### For HCI / Data Collection
- Collect typing metrics in a controlled environment  
- Study user typing behavior  
- Run typing experiments

### For Beginners in Python
- Learn Tkinter event binding  
- Understand file logging  
- Practice dataclasses  
- Study clean project structure

---

## ❓ Troubleshooting

### The GUI doesn’t open
Make sure you're using a standard Python installation with Tkinter.

### Nothing gets logged
You must type **inside the program’s text box**, not elsewhere.

### Log file not found
It will be automatically created in the same folder as the script.

---

## 📌 Project Structure

```
basic-keylogger/
 ├── basic_keylogger.py      # Main program
 ├── basic_keylog.txt        # Log file (auto-created)
 └── README.md               # This file
```



---
````

