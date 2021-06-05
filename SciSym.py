import json
import sys
import time
from pynput import keyboard


class SciSym:
    __version__ = "1.0.0"

    def __init__(self):
        # Create and assign keyboard controller object
        kb = keyboard.Controller()
        self.kb = kb

        shortcuts = json.load(open("shortcuts.json"))

        # Define hotkeys and function
        key_prefix = shortcuts["prefix"]
        hotkeys = {
            f"{key_prefix}+<esc>": self.stop,
            f"{key_prefix}+{shortcuts['unit']['degree']}": self.symbol_degree,
            f"{key_prefix}+{shortcuts['greek']['delta']}": self.symbol_delta,
            f"{key_prefix}+{shortcuts['greek']['delta_lower']}": self.symbol_delta_lower,
            f"{key_prefix}+{shortcuts['greek']['pi']}": self.symbol_pi,
            f"{key_prefix}+{shortcuts['math']['multiply']}": self.symbol_multiply,
            f"{key_prefix}+{shortcuts['math']['plus_minus']}": self.symbol_plus_minus,
            f"{key_prefix}+{shortcuts['math']['less_equal']}": self.symbol_less_equal,
            f"{key_prefix}+{shortcuts['math']['greater_equal']}": self.symbol_greater_equal,
            f"{key_prefix}+{shortcuts['math']['not_equal']}": self.symbol_not_equal,
            f"{key_prefix}+{shortcuts['chem']['reaction_arrow']}": self.symbol_reaction_arrow,
            f"{key_prefix}+{shortcuts['chem']['equilibrium']}": self.symbol_equilibrium,
            f"{key_prefix}+{shortcuts['logic']['therefore']}": self.symbol_therefore,
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

    def symbol_degree(self):
        self.insert_char("°")

    def symbol_delta(self):
        self.insert_char("Δ")

    def symbol_delta_lower(self): self.insert_char("δ")

    def symbol_pi(self): self.insert_char("π")

    def symbol_equilibrium(self): self.insert_char("⇌")

    def symbol_reaction_arrow(self): self.insert_char("⟶")

    def symbol_therefore(self): self.insert_char("∴")

    def symbol_not_equal(self): self.insert_char("≠")

    def symbol_less_equal(self): self.insert_char("≤")

    def symbol_greater_equal(self): self.insert_char("≥")

    def symbol_plus_minus(self): self.insert_char("±")

    def symbol_degree_celsius(self): self.insert_char("℃")

    def symbol_unit_kelvin(self): self.insert_char("K")

    def symbol_multiply(self): self.insert_char("×")
