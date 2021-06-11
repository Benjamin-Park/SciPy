import json
import sys
import time
from pynput import keyboard


class SciSym:
    __version__ = "1.2.0"

    def __init__(self):
        # Create and assign keyboard controller object
        kb = keyboard.Controller()
        self.kb = kb

        shortcuts = json.load(open("shortcuts.json", encoding="utf-8"))

        # Define hotkeys and function
        key_prefix = shortcuts["prefix"]
        hotkeys = {
            f"{key_prefix}+<esc>": self.stop,
        }
        for category in shortcuts:
            if (category != "prefix"):
                for symbol in shortcuts[category]:
                    hotkeys.update({f"{key_prefix}+{shortcuts[category][symbol]['key']}": lambda _char=shortcuts[category][symbol]['char']: self.insert_char(_char)})
        self.hotkeys = hotkeys

        # Listen for hotkeys
        with keyboard.GlobalHotKeys(self.hotkeys) as h:
            h.join()

    @staticmethod
    def stop():
        sys.exit()

    def insert_char(self, _char):
        print(f"Inserted: {_char}")  # Debug log
        self.kb.press(_char)
        time.sleep(0.15)
        self.kb.release(_char)
