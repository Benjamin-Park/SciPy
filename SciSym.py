import json
import sys
import time
from pynput import keyboard


class SciSym:
    __version__ = "1.1.0"

    def __init__(self):
        # Create and assign keyboard controller object
        kb = keyboard.Controller()
        self.kb = kb

        shortcuts = json.load(open("shortcuts.json"))

        # Define hotkeys and function
        key_prefix = shortcuts["prefix"]
        hotkeys = {
            f"{key_prefix}+<esc>": self.stop,
            f"{key_prefix}+{shortcuts['unit']['degree']}": lambda: self.insert_char("°"),
            f"{key_prefix}+{shortcuts['greek']['delta']}": lambda: self.insert_char("Δ"),
            f"{key_prefix}+{shortcuts['greek']['delta_lower']}": lambda: self.insert_char("δ"),
            f"{key_prefix}+{shortcuts['greek']['lambda']}": lambda: self.insert_char("λ"),
            f"{key_prefix}+{shortcuts['greek']['pi']}": lambda: self.insert_char("π"),
            f"{key_prefix}+{shortcuts['math']['multiply']}": lambda: self.insert_char("×"),
            f"{key_prefix}+{shortcuts['math']['plus_minus']}": lambda: self.insert_char("±"),
            f"{key_prefix}+{shortcuts['math']['less_equal']}": lambda: self.insert_char("≤"),
            f"{key_prefix}+{shortcuts['math']['greater_equal']}": lambda: self.insert_char("≥"),
            f"{key_prefix}+{shortcuts['math']['not_equal']}": lambda: self.insert_char("≠"),
            f"{key_prefix}+{shortcuts['chem']['reaction_arrow']}": lambda: self.insert_char("⟶"),
            f"{key_prefix}+{shortcuts['chem']['equilibrium']}": lambda: self.insert_char("⇌"),
            f"{key_prefix}+{shortcuts['logic']['therefore']}": lambda: self.insert_char("∴"),
        }
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
