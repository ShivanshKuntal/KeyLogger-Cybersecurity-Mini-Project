"""
Basic keyboard event logger (for demo/theory use)

- Logs only keys typed inside this program's window
- Shows a visible text box where the user types
- Saves keystrokes with timestamps to a local file
- No background logging, no remote delivery, no OS-wide hooks
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import tkinter as tk


LOG_FILE = Path("basic_keylog.txt")


@dataclass
class KeyEvent:
    timestamp: datetime
    key: str

    def to_log_string(self) -> str:
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time_str}] {self.key}"


class LogManager:
    def __init__(self, log_path: Path):
        self.log_path = log_path
        # Ensure file exists
        if not self.log_path.exists():
            self.log_path.touch()

    def write_event(self, event: KeyEvent) -> None:
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(event.to_log_string() + "\n")


class BasicKeyLoggerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Keyboard Event Demo (Consented Input Only)")

        self.log_manager = LogManager(LOG_FILE)

        info_label = tk.Label(
            root,
            text=(
                "Keyboard Event Demo\n"
                "Type in the box below. Keystrokes are logged with timestamps\n"
                f"to: {LOG_FILE.resolve()}"
            ),
            justify="left"
        )
        info_label.pack(padx=10, pady=10)

        self.text_widget = tk.Text(root, width=60, height=10)
        self.text_widget.pack(padx=10, pady=10)

        # Bind key events only inside this widget
        self.text_widget.bind("<Key>", self.on_key_press)

    def on_key_press(self, event: tk.Event) -> None:
        # event.char may be empty for special keys
        key_repr = event.char if event.char else f"[{event.keysym}]"

        key_event = KeyEvent(
            timestamp=datetime.now(),
            key=key_repr,
        )
        self.log_manager.write_event(key_event)


def main() -> None:
    root = tk.Tk()
    app = BasicKeyLoggerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
