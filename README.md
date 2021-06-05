# SciSym v1.0.0
Insert scientific symbols using customisable keyboard shortcuts.

## Prerequisites
- Python 3.6+
- pynput

## Using SciSym
To launch SciSym execute `main.py`

### Default Shortcut Mappings:

| <hr><h4>**General** ||
| ------- | -------- |
| **Command** | **Shortcut** |
| Exit SciSym Application | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>Esc</kbd> |
| <hr><h4>**Greek Alphabet** ||
| **Command** | **Shortcut** |
| `Δ` Insert `Greek Delta` | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>D</kbd> |
| `δ` Insert `Greek Delta (lowercase)` | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>F</kbd> |
| `π` Insert `Greek Pi (lowercase)` | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>P</kbd> |
| <hr><h4>**Mathematics** ||
| **Command** | **Shortcut** |
| `×` Insert `Multiply` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>M</kbd> |
| `±` Insert `Plus/Minus` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>-</kbd> |
| `≠` Insert `Not Equal` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>N</kbd> |
| `≤` Insert `Less-than or Equal to` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>,</kbd> |
| `≥` Insert `Greater-than or Equal to` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>.</kbd> |
| `°` Insert `Degree` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>A</kbd> |
| <hr><h4>**Chemistry** ||
| **Command** | **Shortcut** |
| `⟶` Insert `Reaction Arrow` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>R</kbd> |
| `⇌` Insert `Equilibrium` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>E</kbd> |
| <hr><h4>**Logic** ||
| **Command** | **Shortcut** |
| `∴` Insert `Therefore` symbol | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd> + <kbd>/</kbd> |

## Customising
Shortcuts can be changed by editing the `shortcuts.json` file. If two or more commands are bound the same shortcut key, only the last one defined in the file will be triggered.
