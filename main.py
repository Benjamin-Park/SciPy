#!/usr/bin/env python3
import SciSym
import update

# Check for updates
update.check_update()
# Start hotkey listener and stuff
ss = SciSym.SciSym()
