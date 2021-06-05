# WARN: Updater is currently in beta

import urllib.request
import json
import SciSym
from distutils import version

AUTO_UPDATE = False
UPDATE_BRANCH = "version_stable"
# UPDATE_BRANCH = "version_beta"  # Uncomment line to opt into beta updates

SCRIPT_FILE = "SciSym.py"
UPDATER_FILE = "update.py"
UPDATER_URL = "https://raw.githubusercontent.com/Benjamin-Park/SciSym/master/version.json"
FILE_URL = "https://raw.githubusercontent.com/Benjamin-Park/SciSym/beta/SciSym.py" if UPDATE_BRANCH == "version_beta" \
    else "https://raw.githubusercontent.com/Benjamin-Park/SciSym/master/SciSym.py"


def check_update():
    try:
        update_manifest = urllib.request.urlopen(UPDATER_URL)
        manifest = json.loads(update_manifest.read())
        if (version.Version(SciSym.SciSym.__version__) < version.Version(manifest[UPDATE_BRANCH])):
            print(
                f"Update Available!\nCurrent version: {SciSym.SciSym.__version__}\nLatest version: {manifest[UPDATE_BRANCH]}")
            if (AUTO_UPDATE):
                print("Updating...")
                get_update()
            return True
        else:
            return False
    except:
        print("Unable to check for updates")


def get_update():
    try:
        urllib.request.urlretrieve(FILE_URL, SCRIPT_FILE)
        print("Update Complete!")
    except:
        print("Update Failed!")
