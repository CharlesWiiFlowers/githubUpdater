import subprocess
import os
import sys
from mod.settings import load_settings
from json import JSONDecodeError
from .mod.github_api import GitHubAPI
from mod.custom_exceptions import InvalidSettingsError

class Updater():
    """Main class for the GHUpdateChecker package."""

    def __init__(self):
        """Initialize the Main class."""

        # Load settings from the JSON file
        try:
            settings = load_settings()

            self.ghUsername = settings[0]
            self.ghRepo = settings[1]
            self.runFile = settings[2]
            self.rootProject = settings[3]
            self.currentVersion = settings[4]
            self.debug = settings[5]
            self.whitelist = settings[6]

        except FileNotFoundError:
            #TODO: Add a autocreation of the settings file if it does not exist
            raise InvalidSettingsError("GHUpdateSettings.json not found. Please ensure it exists in the correct directory.")
        except JSONDecodeError:
            raise InvalidSettingsError("Error decoding GHUpdateSettings.json. Please ensure it is valid JSON.")

        self.github_api = GitHubAPI(self.ghUsername, self.ghRepo)

    def is_update_available(self) -> bool:
        """Check for updates in the GitHub repository."""    
        latest_release = self.github_api.get_latest_release_tag()
        if latest_release and latest_release != self.currentVersion:
            return True
        else:
            return False

    def get_latest_version(self) -> str | type[ConnectionError]:
        """Get the latest version from the GitHub repository."""
        latest_release = self.github_api.get_latest_release_tag()
        
        if latest_release:
            return latest_release
        else:
            return ConnectionError
        
    def install_last_release(self) -> None:
        """Install the update by running the updater script."""

        script_path = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'updater.py')

        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Updater script not found at {script_path}")

        subprocess.Popen([sys.executable, script_path, self.ghUsername, self.ghRepo, self.runFile, self.rootProject, self.currentVersion, self.debug, self.whitelist], cwd=os.path.dirname(__name__))
        sys.exit(0)